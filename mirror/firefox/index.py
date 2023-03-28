import os.path
import re

from tqdm.auto import tqdm

from mirror.utils import get_github_client

_VERSION_PATTERN = re.compile(r'^(v\.|v|Wires\s*|)(?P<version>[\d.]+)$')


def _version_split(v):
    matching = _VERSION_PATTERN.fullmatch(v)
    if matching:
        version_text = matching.group('version')
        return tuple(map(int, version_text.split('.')))
    else:
        raise ValueError(f'Invalid version for firefox release - {v!r}.')


def get_file_list():
    g = get_github_client()
    repo = g.get_repo("mozilla/geckodriver")

    retval = []
    versions = []
    for release in tqdm(repo.get_releases()):
        directory = release.tag_name
        versions.append((release.tag_name, _version_split(release.tag_name)))
        for asset in release.get_assets():
            filename = asset.name
            download_url = asset.browser_download_url
            size = asset.size
            retval.append((download_url, os.path.join(directory, filename), size))

    return retval, versions
