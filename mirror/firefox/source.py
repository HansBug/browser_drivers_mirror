from hfmirror.resource import GithubReleaseResource

from ..utils import get_github_client


class FirefoxResource(GithubReleaseResource):
    def __init__(self):
        GithubReleaseResource.__init__(
            self, "mozilla/geckodriver",
            github_client=get_github_client(),
        )
