import os.path
from functools import partial

import click
from hfmirror.storage import HuggingfaceStorage, LocalStorage
from hfmirror.sync import SyncTask
from huggingface_hub import HfApi

from .source import IEResource
from ..config import DEFAULT_TARGET_REPO, DEFAULT_REPO_TYPE
from ..utils import GLOBAL_CONTEXT_SETTINGS, register_for_hf
from ..utils import print_version as _origin_print_version

print_version = partial(_origin_print_version, 'mirror.ie')


@click.group(context_settings={**GLOBAL_CONTEXT_SETTINGS})
@click.option('-v', '--version', is_flag=True,
              callback=print_version, expose_value=False, is_eager=True,
              help="Utils with ie driver resources.")
def cli():
    pass  # pragma: no cover


@cli.command('trans', help="Transport files to huggingface",
             context_settings={**GLOBAL_CONTEXT_SETTINGS})
@click.option('--repo', '-r', 'repo', type=str, default=DEFAULT_TARGET_REPO,
              help='Repository to upload.', show_default=True)
@click.option('--namespace', '-n', 'namespace', type=str, default='ie',
              help="Namespace to upload.", show_default=True)
def trans(repo: str, namespace: str):
    src = IEResource()

    register_for_hf()
    api = HfApi(token=os.environ['HF_TOKEN'])
    api.create_repo(repo, repo_type=DEFAULT_REPO_TYPE, exist_ok=True)
    storage = HuggingfaceStorage(repo=repo, hf_client=api, namespace=namespace)

    task = SyncTask(src, storage)
    task.sync()


@cli.command('download', help='Download file to local directory',
             context_settings={**GLOBAL_CONTEXT_SETTINGS})
@click.option('--output', '-O', 'output_dir', type=str, required=True,
              help='Directory to download to.', show_default=True)
@click.option('--namespace', '-n', 'namespace', type=str, default='ie',
              help="Namespace to upload.", show_default=True)
def download(output_dir: str, namespace: str):
    os.makedirs(output_dir, exist_ok=True)
    src = IEResource()
    storage = LocalStorage(output_dir, namespace)
    task = SyncTask(src, storage)
    task.sync()


if __name__ == '__main__':
    cli()
