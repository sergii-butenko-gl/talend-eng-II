import pytest


# test must start with test_ wording
def test_sing_up_positive(user_fixture):
    print("SIGNUP TEST POSITIVE")
    user_fixture.name = "Hello"
    assert user_fixture.name == "Hello"


@pytest.mark.xfail
def test_sing_up_negative(user_fixture):
    print("SIGNUP TEST NEGATIVE")
    assert user_fixture.name != "sergii"
