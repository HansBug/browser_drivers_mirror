import os
import pathlib
from functools import partial

import click
import requests
from hbutils.string import env_template
from huggingface_hub import hf_hub_url
from tqdm.auto import tqdm

from .utils import GLOBAL_CONTEXT_SETTINGS
from .utils import print_version as _origin_print_version

print_version = partial(_origin_print_version, 'mirror')


@click.group(context_settings={**GLOBAL_CONTEXT_SETTINGS}, help='Global Utils')
@click.option('-v', '--version', is_flag=True,
              callback=print_version, expose_value=False, is_eager=True,
              help="Show version.")
def cli():
    pass  # pragma: no cover


def _get_latest_release_version(b) -> str:
    if b == 'edge':
        resp = requests.get(hf_hub_url(repo_id='HansBug/browser_drivers_mirror', filename='edge/LATEST_STABLE'))
        return resp.content.decode('utf-16').strip()
    else:
        resp = requests.get(hf_hub_url(repo_id='HansBug/browser_drivers_mirror', filename=f'{b}/LATEST_RELEASE'))
        return resp.text.strip()


_UNKNOWN_BROWSERS = ['google', 'firefox', 'edge', 'opera']


@cli.command('readme', help='Regenerate README.md.',
             context_settings={**GLOBAL_CONTEXT_SETTINGS})
@click.option('--template', '-t', 'template_filename', type=click.Path(exists=True, dir_okay=False, readable=True),
              default='README.template.md', help='Template file of README.md', show_default=True)
@click.option('--output', '-o', 'output', type=click.Path(dir_okay=False), default='README.md',
              help='Output file of README.md.', show_default=True)
@click.option('--huggingface', '-H', 'is_huggingface', is_flag=True, type=bool, default=False,
              help='Is huggingface\'s readme or not.', show_default=True)
@click.option('--scheme_template', '-s', 'scheme_template_filename',
              type=click.Path(exists=True, dir_okay=False, readable=True),
              default='README_scheme.template.md', help='Scheme template file of README.md (required on huggingface)',
              show_default=True)
def readme(template_filename: str, output: str, is_huggingface: bool, scheme_template_filename: str):
    envs = {}
    for browser in tqdm(_UNKNOWN_BROWSERS):
        envs[f'{browser.upper()}_LATEST_RELEASE'] = _get_latest_release_version(browser)
    envs = {**os.environ, **envs}

    if is_huggingface:
        scheme_template = pathlib.Path(scheme_template_filename).read_text()
        scheme_text = env_template(scheme_template, environ=envs, safe=True, default='')
    else:
        scheme_text = None

    template = pathlib.Path(template_filename).read_text()
    readme_text = env_template(template, environ=envs, safe=True, default='')
    with open(output, 'w') as f:
        if is_huggingface:
            f.write(scheme_text)
            f.write(os.linesep)
        f.write(readme_text)


if __name__ == '__main__':
    cli()