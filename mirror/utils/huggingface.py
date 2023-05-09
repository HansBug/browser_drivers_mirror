import os
from functools import partial
from typing import Dict
from typing import Optional
from urllib.parse import quote

from hfmirror.utils import get_requests_session
from hfmirror.utils.session import DEFAULT_TIMEOUT
from huggingface_hub import HfApi, configure_http_backend
from huggingface_hub.constants import ENDPOINT, REPO_TYPES, REPO_TYPES_URL_PREFIXES, DEFAULT_REVISION
from huggingface_hub.utils import validate_hf_hub_args


def get_huggingface_client(access_token=None):
    access_token = access_token or os.environ.get('HF_TOKEN', None)
    return HfApi(token=access_token)


def register_for_hf(max_retries: int = 5, timeout: int = DEFAULT_TIMEOUT,
                    headers: Optional[Dict[str, str]] = None):
    configure_http_backend(backend_factory=partial(get_requests_session, max_retries, timeout, headers))


HUGGINGFACE_CO_TREE_URL_TEMPLATE = ENDPOINT + "/{repo_id}/tree/{revision}/{filename}"


@validate_hf_hub_args
def hf_hub_tree_url(
        repo_id: str,
        filename: str,
        *,
        subfolder: Optional[str] = None,
        repo_type: Optional[str] = None,
        revision: Optional[str] = None,
) -> str:
    if subfolder == "":
        subfolder = None
    if subfolder is not None:
        filename = f"{subfolder}/{filename}"

    if repo_type not in REPO_TYPES:
        raise ValueError("Invalid repo type")

    if repo_type in REPO_TYPES_URL_PREFIXES:
        repo_id = REPO_TYPES_URL_PREFIXES[repo_type] + repo_id

    if revision is None:
        revision = DEFAULT_REVISION
    return HUGGINGFACE_CO_TREE_URL_TEMPLATE.format(
        repo_id=repo_id,
        revision=quote(revision, safe=""),
        filename=quote(filename),
    )
