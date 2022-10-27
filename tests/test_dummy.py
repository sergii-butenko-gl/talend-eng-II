def somefunction():
    assert True is True


def test_always_passes():
    assert True is True


def test_always_failed():
    assert False


def always_passes_test():
    assert True is True
    # /\ is the same as \/    
    # if True is not True:
    #     raise ValidationError("Is not equal")
