"""This module tests that the Singleton correctly implements the pattern."""


from syngle.decorator import singleton


def test_check_same_identity_decorator():
    """Checks that instantiating the _Dummy class always returns the same object."""

    @singleton
    class _DummyDecoratedClass:
        pass

    obj1 = _DummyDecoratedClass()
    obj2 = _DummyDecoratedClass()

    assert obj1 is obj2


def test_check_same_identity_decorator_args():
    """Checks that instantiating the _Dummy class always returns the same object."""

    @singleton
    class _DummyDecoratedClass:
        def __init__(self, *args):
            self.args = args

    a_args = (0, 1, 2)
    b_args = (1, 2, 3)

    obj1 = _DummyDecoratedClass(*a_args)
    obj2 = _DummyDecoratedClass(*b_args)

    assert obj1.args == a_args == obj2.args
    assert obj1 is obj2


def test_check_same_identity_decorator_kwargs():
    """Checks that instantiating the _Dummy class always returns the same object."""

    @singleton
    class _DummyDecoratedClass:
        def __init__(self, **kwargs):
            self.kwargs = kwargs

    a_kwargs = {"arg": 0}
    b_kwargs = {"arg": 1}

    obj1 = _DummyDecoratedClass(**a_kwargs)
    obj2 = _DummyDecoratedClass(**b_kwargs)

    assert obj1.kwargs == a_kwargs == obj2.kwargs
    assert obj1 is obj2


def test_check_same_identity_decorator_args_kwargs():
    """Checks that instantiating the _Dummy class always returns the same object."""

    @singleton
    class _DummyDecoratedClass:
        def __init__(self, *args, **kwargs) -> None:

            self.args = args
            self.kwargs = kwargs

    a_args = (0, 1, 2)
    b_args = (1, 2, 3)

    a_kwargs = {"arg": 0}
    b_kwargs = {"arg": 1}

    obj1 = _DummyDecoratedClass(*a_args, **a_kwargs)
    obj2 = _DummyDecoratedClass(*b_args, **b_kwargs)

    assert obj1.args == a_args == obj2.args
    assert obj1.kwargs == a_kwargs == obj2.kwargs
    assert obj1 is obj2
