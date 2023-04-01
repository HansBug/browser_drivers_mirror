import logging
import os
import pathlib
from functools import partial
from unittest.mock import patch

import click
import requests
from hbutils.string import env_template
from huggingface_hub import hf_hub_url
from tqdm.auto import tqdm
from webdriver_manager.core.utils import os_type
from webdriver_manager.dispatch import get_browser_manager

from .utils import GLOBAL_CONTEXT_SETTINGS, get_huggingface_client
from .utils import print_version as _origin_print_version

print_version = partial(_origin_print_version, 'mirror')


def _get_latest_release_version(b) -> str:
    if b == 'edge':
        resp = requests.get(hf_hub_url(repo_id='HansBug/browser_drivers_mirror', filename=f'{b}/LATEST_STABLE'))
        return resp.text.strip()
    else:
        resp = requests.get(hf_hub_url(repo_id='HansBug/browser_drivers_mirror', filename=f'{b}/LATEST_RELEASE'))
        return resp.text.strip()


@click.group(context_settings={**GLOBAL_CONTEXT_SETTINGS}, help='Global Utils')
@click.option('-v', '--version', is_flag=True,
              callback=print_version, expose_value=False, is_eager=True,
              help="Show version.")
def cli():
    pass  # pragma: no cover


_UNKNOWN_BROWSERS = ['google', 'firefox', 'edge', 'opera', 'ie']


def _get_envs_of_release_urls():
    url_records = {}
    items = []
    for os_ in ['linux', 'darwin', 'win32']:
        for bits in [32, 64]:
            for is_arch in [True, False]:
                for browser_name in _UNKNOWN_BROWSERS:
                    if browser_name == 'ie' and os_ != 'win32':
                        continue
                    if os_ != 'win32' and bits == 32:
                        continue
                    if browser_name == 'chrome' and bits == 32:
                        continue
                    if is_arch and (os_ != 'darwin' or browser_name not in ['chrome', 'firefox']):
                        continue

                    items.append((os_, bits, is_arch, browser_name))

    for os_, bits, is_arch, browser_name in tqdm(items):
        with patch('sys.platform', os_), patch('platform.machine', lambda: f'{bits}'), \
                patch('platform.processor', lambda: 'i386' if not is_arch else 'x86_64'):
            driver = get_browser_manager(browser_name)
            try:
                name = f'{browser_name}_{os_type()}'
                if is_arch:
                    name = f'{name}_arch'
                name = f'{name}_url'.upper()
                url_records[name] = driver.driver_url
            except ValueError:
                logging.warning(f'No driver found for {browser_name} on {os_type()}.')

    return url_records


def _get_envs_of_versions():
    envs = {}
    for browser in tqdm(_UNKNOWN_BROWSERS):
        envs[f'{browser.upper()}_LATEST_RELEASE'] = _get_latest_release_version(browser)
    return envs


def _get_envs_for_render():
    return {
        **os.environ,
        **_get_envs_of_versions(),
        **_get_envs_of_release_urls()
    }


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
    envs = _get_envs_for_render()
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


@cli.command('hf_readme', help='Regenerate README.md for huggingface, and then upload it.',
             context_settings={**GLOBAL_CONTEXT_SETTINGS})
@click.option('--input', '-i', 'readme_filename', type=click.Path(exists=True, file_okay=True, readable=True),
              required=True, help='README.md file to upload.', show_default=True)
@click.option('--repo', '-r', 'repo', type=str, default='HansBug/browser_drivers_mirror',
              help='Repository to upload.', show_default=True)
@click.option('--remote', '-R', 'remote_filename', type=str, default='README.md',
              help='README.md file in repository.', show_default=True)
def hf_readme(readme_filename: str, repo: str, remote_filename: str):
    resp = requests.get(hf_hub_url(repo_id=repo, filename=remote_filename))
    resp.raise_for_status()

    remote_readme_text = resp.text
    local_readme_text = pathlib.Path(readme_filename).read_text()
    if remote_readme_text != local_readme_text:
        api = get_huggingface_client()
        api.upload_file(
            path_or_fileobj=readme_filename,
            path_in_repo=remote_filename,
            repo_id=repo,
            repo_type='model',
        )


if __name__ == '__main__':
    cli()
