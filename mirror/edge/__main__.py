import os.path
from functools import partial

import click
from tqdm.auto import tqdm

from mirror.utils import GLOBAL_CONTEXT_SETTINGS
from mirror.utils import file_download
from mirror.utils import print_version as _origin_print_version
from .index import get_file_list, EDGE_DRIVE_ROOT

print_version = partial(_origin_print_version, 'mirror.edge')


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
def export(output_dir: str):
    click.echo(click.style(f'Getting index from {EDGE_DRIVE_ROOT!r} ...'))
    for url, filename, filesize in tqdm(get_file_list()):
        click.echo(f'Downloading {url} ...')
        file_download(url, os.path.join(output_dir, filename), expected_size=filesize)


if __name__ == '__main__':
    cli()
