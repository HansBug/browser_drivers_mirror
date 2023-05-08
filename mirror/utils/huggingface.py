import os
from functools import partial
from typing import Optional, Dict

from hfmirror.utils import get_requests_session
from hfmirror.utils.session import DEFAULT_TIMEOUT
from huggingface_hub import HfApi, configure_http_backend


def get_huggingface_client(access_token=None):
    access_token = access_token or os.environ.get('HF_TOKEN', None)
    return HfApi(token=access_token)


def register_for_hf(max_retries: int = 5, timeout: int = DEFAULT_TIMEOUT,
                    headers: Optional[Dict[str, str]] = None):
    configure_http_backend(backend_factory=partial(get_requests_session, max_retries, timeout, headers))
