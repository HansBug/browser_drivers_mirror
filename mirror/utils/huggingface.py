import os

import requests
from huggingface_hub import HfApi, hf_hub_url


def get_huggingface_client(access_token=None):
    access_token = access_token or os.environ.get('HF_TOKEN', None)
    return HfApi(token=access_token)


def is_file_exist_in_repo(repo_id, filename, max_tries: int = 5):
    for _ in range(max_tries):
        try:
            return requests.head(hf_hub_url(repo_id=repo_id, filename=filename)).ok
        except ConnectionError:
            continue
    else:
        return False
