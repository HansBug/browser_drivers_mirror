import os
import xml.etree.ElementTree as ET

import requests

from ..utils import etree_to_dict

GOOGLE_DRIVE_ROOT = 'https://chromedriver.storage.googleapis.com'


def get_file_list():
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
    retval = []
    for item in contents:
        file_url_name = item['Key']
        file_size = int(item['Size'])

        url = f'{GOOGLE_DRIVE_ROOT}/{file_url_name}'
        relpath = os.sep.join(file_url_name.split('/'))
        retval.append((url, relpath, file_size))

    return retval
