import os
import xml.etree.ElementTree as ET
from typing import Iterable, Union, Tuple, Any, Mapping

import requests
from hfmirror.resource import SyncResource, RemoteSyncItem
from hfmirror.resource.item import register_sync_type
from hfmirror.utils import TargetPathType

from ..utils import etree_to_dict

GOOGLE_DRIVE_ROOT = 'https://chromedriver.storage.googleapis.com'


class StripSyncItem(RemoteSyncItem):
    __type__ = 'strip'

    def _file_process(self, filename):
        fn = os.path.basename(filename)
        if fn.startswith('LATEST'):
            with open(filename, 'r') as f:
                text = f.read()
            with open(filename, 'w') as f:
                f.write(text.strip())


register_sync_type(StripSyncItem)


class ChromeResource(SyncResource):
    def grab(self) -> Iterable[Union[
        Tuple[str, Any, TargetPathType, Mapping],
        Tuple[str, Any, TargetPathType],
    ]]:
        resp = requests.get(GOOGLE_DRIVE_ROOT)
        xml_str = resp.text

        # 解析XML文本为ElementTree对象
        root = ET.fromstring(xml_str)
        for elem in root.iter():
            if not hasattr(elem.tag, 'find'): continue
            i = elem.tag.find('}')
            if i >= 0:
                elem.tag = elem.tag[i + 1:]

        json = etree_to_dict(root)
        assert "ListBucketResult" in json
        assert json["ListBucketResult"]["Name"] == "chromedriver"

        contents = json["ListBucketResult"]["Contents"]
        for item in contents:
            file_url_name = item['Key']
            url = f'{GOOGLE_DRIVE_ROOT}/{file_url_name}'
            relpath = os.sep.join(file_url_name.split('/'))
            yield 'strip', url, relpath, {}
