from hfmirror.resource import GithubReleaseResource

from ..utils import get_github_client


class IEResource(GithubReleaseResource):
    def __init__(self):
        GithubReleaseResource.__init__(
            self, "SeleniumHQ/selenium",
            github_client=get_github_client(),
        )

    def _tag_filter(self, tag):
        if 'alpha' in tag or 'beta' in tag or 'rc' in tag:
            return None
        else:
            return tag

    def _filename_filter(self, tag, filename):
        if filename.startswith('IEDriverServer'):
            return filename
        else:
            return None
