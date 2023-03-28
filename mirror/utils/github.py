import os

from github import Github


def get_github_client(access_token=None) -> Github:
    access_token = access_token or os.environ.get('GITHUB_ACCESS_TOKEN', None)
    return Github(access_token)
