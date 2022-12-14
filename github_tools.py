from functools import cache

import github
import pickle
import pathlib
import datetime
import dotenv
import os

dotenv.load_dotenv()
OWNER_NAME = 'Alyce Osbourne'
REPO_OWNER = OWNER_NAME.replace(" ", "")
gh_token = os.getenv("GITHUB_TOKEN")
gh = github.Github(gh_token)
owner = gh.get_user(REPO_OWNER)
repos = owner.get_repos()
cache_path = pathlib.Path("cache")
cache_path.mkdir(exist_ok = True)


@cache
def get_repos_for_user(user):
    return user.get_repos(sort = "updated", direction = "desc")[0:3]


def get_repos():
    return get_repos_for_user(owner)
