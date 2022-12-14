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


def get_repos_for_user(user):
    if not (cache_path / "most_active_projects.pkl").exists() or (
            datetime.datetime.now() - datetime.datetime.fromtimestamp(
            (cache_path / "most_active_projects.pkl").stat().st_mtime)).days > 1:
        most_active_projects = user.get_repos(sort = "updated", direction = "desc")[0:3]
        with open(cache_path / "most_active_projects.pkl", "wb") as f:
            pickle.dump(most_active_projects, f)
    else:
        with open(cache_path / "most_active_projects.pkl", "rb") as f:
            most_active_projects = pickle.load(f)
    return most_active_projects


def get_repos():
    return get_repos_for_user(owner)
