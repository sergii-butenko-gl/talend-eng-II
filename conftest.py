from src.applications.GitHubApi import GitHubApi
from src.models.user import User
from src.config.config import Config, JSONConfigProvider, OSConfigProvider

import pytest

config = Config([OSConfigProvider, JSONConfigProvider])


@pytest.fixture(scope="session")
def database_connection():
    print("ESTABLISH DB CONNECTION")
    yield "CONNECTION OBJECT"
    print("CLOSE DB CONNECTION")


@pytest.fixture(scope="class")
def user_fixture():
    user = User(config.SHARED_USER_NAME, config.SHARED_EMAIL)
    # user.create_in_database()

    yield user

    # user.remove_from_database()


@pytest.fixture
def github_api():
    github_api = GitHubApi()
    if github_api.login('user') is False:
        raise Exception("User's login failed")

    yield github_api

    github_api.logout()
