import os.path
import tempfile
from functools import partial

import click
from huggingface_hub import hf_hub_url
from tqdm.auto import tqdm

from .index import get_file_list, EDGE_DRIVE_ROOT
from ..utils import GLOBAL_CONTEXT_SETTINGS, get_huggingface_client, file_download, is_file_exist_in_repo
from ..utils import print_version as _origin_print_version

print_version = partial(_origin_print_version, 'mirror.edge')


def _latest_preprocess(file):
    with open(file, 'rb') as f:
        binary = f.read()
    with open(file, 'w') as f:
        f.write(binary.decode('utf-16').strip())


@click.group(context_settings={**GLOBAL_CONTEXT_SETTINGS})
@click.option('-v', '--version', is_flag=True,
              callback=print_version, expose_value=False, is_eager=True,
              help="Utils with edge driver resources.")
def cli():
    pass  # pragma: no cover


@cli.command('download', help='Download all files on edge\'s official driver page.',
             context_settings={**GLOBAL_CONTEXT_SETTINGS})
@click.option('--output_dir', '-O', 'output_dir', type=click.Path(file_okay=False), required=True,
              help='Output directory of all models.', show_default=True)
def download(output_dir: str):
    click.echo(click.style(f'Getting index from {EDGE_DRIVE_ROOT!r} ...'))
    for url, filename, filesize in tqdm(get_file_list()):
        click.echo(f'Downloading {url} ...')
        file_download(url, os.path.join(output_dir, filename), expected_size=filesize)


@cli.command('trans', help="Transport files to huggingface",
             context_settings={**GLOBAL_CONTEXT_SETTINGS})
@click.option('--repo', '-r', 'repo', type=str, default='HansBug/browser_drivers_mirror',
              help='Repository to upload.', show_default=True)
@click.option('--namespace', '-n', 'namespace', type=str, default='edge',
              help="Namespace to upload.", show_default=True)
def trans(repo: str, namespace: str):
    api = get_huggingface_client()
    with tempfile.TemporaryDirectory() as root_td:
        for url, filename, filesize in tqdm(get_file_list()):
            _directory, _ = os.path.split(filename)
            if _directory:
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
            else:
                local_filename = os.path.join(root_td, os.path.basename(url))
                file_download(url, local_filename, filesize)
                if os.path.basename(local_filename).startswith('LATEST_'):
                    _latest_preprocess(local_filename)

        api.upload_folder(
            folder_path=root_td,
            path_in_repo=namespace,
            repo_id=repo,
            repo_type='model',
        )


@cli.command('index', help='Index all files on edge\'s official driver page.',
             context_settings={**GLOBAL_CONTEXT_SETTINGS})
@click.option('--repo', '-r', 'repo', type=str, default='HansBug/browser_drivers_mirror',
              help='Repository to upload.', show_default=True)
@click.option('--namespace', '-n', 'namespace', type=str, default='edge',
              help="Namespace to upload.", show_default=True)
@click.option('--output_dir', '-O', 'output_dir', type=click.Path(file_okay=False), required=True,
              help='Output directory of all models.', show_default=True)
def index(repo: str, namespace: str, output_dir: str):
    click.echo(click.style(f'Getting index from {EDGE_DRIVE_ROOT!r} ...'))
    os.makedirs(output_dir, exist_ok=True)
    for url, filename, filesize in tqdm(get_file_list()):
        _directory, _ = os.path.split(filename)
        index_filename = os.path.join(output_dir, filename)
        _index_dir, _ = os.path.split(index_filename)
        if _index_dir:
            os.makedirs(_index_dir, exist_ok=True)

        if _directory:
            index_filename = f'{index_filename}_index'
            with open(index_filename, 'w') as f:
                f.write(hf_hub_url(repo, f'{namespace}/{filename}', repo_type='model'))
        else:
            file_download(url, index_filename, filesize)
            if os.path.basename(index_filename).startswith('LATEST_'):
                _latest_preprocess(index_filename)


if __name__ == '__main__':
    cli()
