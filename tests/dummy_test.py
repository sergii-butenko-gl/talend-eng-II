# not a test
def somefunction():
    assert True is True


# test must start with test_ wording
def test_always_passes():
    assert (1, 2, 3) == (3, 2, 1)


def test_always_passes_2():
    assert (1, 2, 3) == (1, 2, 3)


# not a test
def always_passes_test():
    assert True is True
