from hfmirror.resource import GithubReleaseResource

from ..utils import get_github_client


class OperaResource(GithubReleaseResource):
    def __init__(self):
        GithubReleaseResource.__init__(
            self, "operasoftware/operachromiumdriver",
            github_client=get_github_client(),
        )
