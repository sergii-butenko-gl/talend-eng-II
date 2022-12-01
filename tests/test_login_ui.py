def test_first_login_test(github_ui_app):
    assert github_ui_app.get_title() == "Sign in to GitHub · GitHub"
