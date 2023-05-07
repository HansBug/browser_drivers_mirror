import os
import time
import xml.etree.ElementTree as ET
from typing import Iterable, Union, Tuple, Any, Mapping

import requests
from hfmirror.resource import SyncResource, RemoteSyncItem
from hfmirror.resource.item import register_sync_type
from hfmirror.utils import TargetPathType
from tqdm.auto import tqdm

from ..utils import etree_to_dict

EDGE_DRIVE_ROOT = 'https://msedgewebdriverstorage.blob.core.windows.net'


class RecodeSyncItem(RemoteSyncItem):
    __type__ = 'recode'

    def _file_process(self, filename):
        fn = os.path.basename(filename)
        if fn.startswith('LATEST'):
            with open(filename, 'rb') as f:
                binary = f.read()
            with open(filename, 'w') as f:
                f.write(binary.decode('utf-16').strip())


register_sync_type(RecodeSyncItem)


class EdgeResource(SyncResource):
    def _grab_layer(self, prefix: str = ''):
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
                yield 'recode', url, filename, {}

            dirs = result["Blobs"].get("BlobPrefix", None) or []
            if isinstance(dirs, dict):
                dirs = [dirs]
            for item in tqdm(dirs):
                yield from self._grab_layer(item['Name'])

            if marker is None:
                break

    def grab(self) -> Iterable[Union[
        Tuple[str, Any, TargetPathType, Mapping],
        Tuple[str, Any, TargetPathType],
    ]]:
        yield from self._grab_layer()
