from src.config.config import config


def test_first_login_test(github_ui_app):
    github_ui_app.goto_login_page()
    github_ui_app.login(config.SHARED_USER_NAME, config.SHARED_USER_PASSWORD)
    # assert github_ui_app.check_title() == "SOME TITLE"


def test_first_logout_test(github_ui_app):
    pass
