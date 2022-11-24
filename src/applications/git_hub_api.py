from src.applications.URLS import URLS
import requests
from src.config.config import config

from urllib.parse import urljoin


class GitHubApi:
    DEFAULT_ACCEPT_HEADER = {"accept": "application/vnd.github+json"}

    def __init__(self) -> None:
        pass

    def _form_url(self, path):
        return urljoin(config.BASE_URL, path)

    def logout(self) -> bool:
        print("LOGOUT HTTP REQUESTS")
        return True

    def login(self, user: str) -> bool:
        print("LOGIN HTTP REQUESTS")
        return True

    def search_repo(self, repo_name: str) -> dict:
        r = requests.get(
            url=self._form_url(URLS.search),
            headers=self.DEFAULT_ACCEPT_HEADER,
            params={"q": repo_name},
        )

        r.raise_for_status()

        return r.json()
