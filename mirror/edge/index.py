import time
import xml.etree.ElementTree as ET

import requests
from tqdm.auto import tqdm

from mirror.utils import etree_to_dict

EDGE_DRIVE_ROOT = 'https://msedgewebdriverstorage.blob.core.windows.net'


def _iter_resource(prefix=''):
    marker = None
    while True:
        resp = requests.get(
            f'{EDGE_DRIVE_ROOT}/edgewebdriver',
            params={
                'delimiter': '/',
                'prefix': prefix,
                'marker': marker,
                'maxresults': '5000',
                'restype': 'container',
                'comp': 'list',
                '_': int(time.time() * 1000),
                'timeout': '60000',
            }
        )
        resp.raise_for_status()

        xml = ET.fromstring(resp.text)
        json_ = etree_to_dict(xml)
        result = json_["EnumerationResults"]
        marker = result["NextMarker"]

        files = result["Blobs"].get("Blob", None) or []
        if isinstance(files, dict):
            files = [files]
        for item in files:
            url = item["Url"]
            filename = item["Name"]
            size = int(item["Properties"]["Content-Length"])
            yield url, filename, size

        dirs = result["Blobs"].get("BlobPrefix", None) or []
        if isinstance(dirs, dict):
            dirs = [dirs]
        for item in tqdm(dirs):
            yield from _iter_resource(item['Name'])

        if marker is None:
            break


def get_file_list():
    return list(_iter_resource())
