import os

def somefunction():
    assert True is True


def test_always_passes():
    user = os.getenv("USERNAME", None)
    assert user == "USER_A"


def test_always_failed():
    assert False


def always_passes_test():
    assert True is True
    # /\ is the same as \/    
    # if True is not True:
    #     raise ValidationError("Is not equal")
