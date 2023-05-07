import os.path
from functools import partial

import click
from hfmirror.storage import HuggingfaceStorage
from hfmirror.sync import SyncTask
from huggingface_hub import HfApi

from .source import FirefoxResource
from ..utils import GLOBAL_CONTEXT_SETTINGS
from ..utils import print_version as _origin_print_version

print_version = partial(_origin_print_version, 'mirror.firefox')


@click.group(context_settings={**GLOBAL_CONTEXT_SETTINGS})
@click.option('-v', '--version', is_flag=True,
              callback=print_version, expose_value=False, is_eager=True,
              help="Utils with firefox driver resources.")
def cli():
    pass  # pragma: no cover


@cli.command('trans', help="Transport files to huggingface",
             context_settings={**GLOBAL_CONTEXT_SETTINGS})
@click.option('--repo', '-r', 'repo', type=str, default='HansBug/browser_drivers_mirror',
              help='Repository to upload.', show_default=True)
@click.option('--namespace', '-n', 'namespace', type=str, default='firefox',
              help="Namespace to upload.", show_default=True)
def trans(repo: str, namespace: str):
    src = FirefoxResource()

    api = HfApi(token=os.environ['HF_TOKEN'])
    api.create_repo(repo, repo_type='dataset', exist_ok=True)
    storage = HuggingfaceStorage(repo=repo, hf_client=api, namespace=namespace)

    task = SyncTask(src, storage)
    task.sync()


if __name__ == '__main__':
    cli()
