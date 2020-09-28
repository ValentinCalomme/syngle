"""This module tests that the Singleton correctly implements the pattern."""


from syngle.singleton import Singleton


class _Dummy(Singleton):
    pass


def test_check_same_identity():
    """Checks that instantiating the _Dummy class always returns the same object."""
    obj1 = _Dummy()
    obj2 = _Dummy()

    assert obj1 is obj2
    assert id(obj1) == id(obj2)
