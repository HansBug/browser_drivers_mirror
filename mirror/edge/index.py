import os
import xml.etree.ElementTree as ET

import requests

from ..utils import etree_to_dict

EDGE_DRIVE_ROOT = 'https://msedgedriver.azureedge.net/'


def get_file_list():
    while True:
        resp = requests.get(EDGE_DRIVE_ROOT, headers={
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;'
                      'q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/105.0.0.0 Safari/537.36',
        })
        if resp.ok:
            break
    xml_str = resp.text

    # 解析XML文本为ElementTree对象
    root = ET.fromstring(xml_str)
    json = etree_to_dict(root)
    retval = []
    for item in json["EnumerationResults"]["Blobs"]["Blob"]:
        relpath = os.sep.join(item["Name"].split('/'))
        url = item['Url']
        size = int(item["Properties"]["Content-Length"])
        retval.append((url, relpath, size))

    return retval
