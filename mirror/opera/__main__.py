import os.path
import tempfile
from functools import partial

import click
from tqdm.auto import tqdm

from .index import get_file_list
from ..utils import GLOBAL_CONTEXT_SETTINGS, get_huggingface_client, is_file_exist_in_repo
from ..utils import file_download
from ..utils import print_version as _origin_print_version

print_version = partial(_origin_print_version, 'mirror.opera')


def _create_version_files(versions, directory):
    version_map = {}
    for version_name, version_tuple in versions:
        for i in range(len(version_tuple) + 1):
            key = '.'.join(map(str, version_tuple[:i]))

            need_set = False
            if key not in version_map:
                need_set = True
            else:
                _, vt = version_map[key]
                if vt < version_tuple:
                    need_set = True

            if need_set:
                version_map[key] = (version_name, version_tuple)

    os.makedirs(directory, exist_ok=True)
    for key, (version_name, _) in version_map.items():
        filename = 'LATEST_RELEASE' if not key else f'LATEST_RELEASE_{key}'
        with open(os.path.join(directory, filename), 'w') as f:
            f.write(version_name)


@click.group(context_settings={**GLOBAL_CONTEXT_SETTINGS})
@click.option('-v', '--version', is_flag=True,
              callback=print_version, expose_value=False, is_eager=True,
              help="Utils with opera driver resources.")
def cli():
    pass  # pragma: no cover


@cli.command('download', help='Download all files on opera\'s official driver page.',
             context_settings={**GLOBAL_CONTEXT_SETTINGS})
@click.option('--output_dir', '-O', 'output_dir', type=click.Path(file_okay=False), required=True,
              help='Output directory of all models.', show_default=True)
def download(output_dir: str):
    click.echo(click.style(f'Getting index from {"github.com"!r} ...'))

    downloads, versions = get_file_list()

    version_map = {}
    for version_name, version_tuple in versions:
        for i in range(len(version_tuple) + 1):
            key = '.'.join(map(str, version_tuple[:i]))

            need_set = False
            if key not in version_map:
                need_set = True
            else:
                _, vt = version_map[key]
                if vt < version_tuple:
                    need_set = True

            if need_set:
                version_map[key] = (version_name, version_tuple)

    os.makedirs(output_dir, exist_ok=True)
    for key, (version_name, _) in version_map.items():
        filename = 'LATEST_RELEASE' if not key else f'LATEST_RELEASE_{key}'
        with open(os.path.join(output_dir, filename), 'w') as f:
            f.write(version_name)

    for url, filename, filesize in tqdm(downloads):
        click.echo(f'Downloading {url} ...')
        file_download(url, os.path.join(output_dir, filename), expected_size=filesize)


@cli.command('trans', help="Transport files to huggingface",
             context_settings={**GLOBAL_CONTEXT_SETTINGS})
@click.option('--repo', '-r', 'repo', type=str, default='HansBug/browser_drivers_mirror',
              help='Repository to upload.', show_default=True)
@click.option('--namespace', '-n', 'namespace', type=str, default='opera',
              help="Namespace to upload.", show_default=True)
def trans(repo: str, namespace: str):
    api = get_huggingface_client()
    downloads, versions = get_file_list()
    for url, filename, filesize in tqdm(downloads):
        if is_file_exist_in_repo(repo_id=repo, filename=f'{namespace}/{filename}'):
            continue

        with tempfile.TemporaryDirectory() as td:
            local_filename = os.path.join(td, os.path.basename(url))
            file_download(url, local_filename, filesize)
            api.upload_file(
                path_or_fileobj=local_filename,
                path_in_repo=f'{namespace}/{filename}',
                repo_id=repo,
                repo_type='model',
            )

    with tempfile.TemporaryDirectory() as td:
        _create_version_files(versions, td)
        api.upload_folder(
            folder_path=td,
            path_in_repo=namespace,
            repo_id=repo,
            repo_type='model',
        )


if __name__ == '__main__':
    cli()
