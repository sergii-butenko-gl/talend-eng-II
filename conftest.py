from src.providers.browsers.browsers_provider import BrowserProvider
from src.applications.git_hub_ui import GitHubUI
from src.applications.git_hub_api import GitHubApi
from src.models.user import User
from src.config.config import config

import pytest


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


@pytest.fixture
def github_ui_app(request):

    # browser = request.config.getoption("--browser")
    browser = config.BROWSER
    driver = BrowserProvider.get_driver(browser_name=browser)

    github_ui_app = GitHubUI(driver)
    github_ui_app.open_base_page()

    yield github_ui_app


# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser",
#         action="store",
#         choices=["chrome", "firefox", "edge"],
#         default="chrome",
#         help="choose firefox or chrome",
#     )