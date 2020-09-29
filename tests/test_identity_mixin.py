"""This module tests that the Singleton correctly implements the pattern."""


from syngle.metaclass import Singleton


def test_check_same_identity_metaclass():
    """Checks that instantiating the _Dummy class always returns the same object."""

    class _DummyMixinClass(metaclass=Singleton):
        pass

    obj1 = _DummyMixinClass()
    obj2 = _DummyMixinClass()

    assert obj1 is obj2


def test_check_same_identity_metaclass_args():
    """Checks that instantiating the _Dummy class always returns the same object."""

    class _DummyMixinClasss(metaclass=Singleton):
        def __init__(self, *args):
            self.args = args

    a_args = (0, 1, 2)
    b_args = (1, 2, 3)

    obj1 = _DummyMixinClasss(*a_args)
    obj2 = _DummyMixinClasss(*b_args)

    assert obj1.args == a_args == obj2.args
    assert obj1 is obj2


def test_check_same_identity_metaclass_kwargs():
    """Checks that instantiating the _Dummy class always returns the same object."""

    class _DummyMixinClasss(metaclass=Singleton):
        def __init__(self, **kwargs):
            self.kwargs = kwargs

    a_kwargs = {"arg": 0}
    b_kwargs = {"arg": 1}

    obj1 = _DummyMixinClasss(**a_kwargs)
    obj2 = _DummyMixinClasss(**b_kwargs)

    assert obj1.kwargs == a_kwargs == obj2.kwargs
    assert obj1 is obj2


def test_check_same_identity_metaclass_args_kwargs():
    """Checks that instantiating the _Dummy class always returns the same object."""

    class _DummyMixinClasss(metaclass=Singleton):
        def __init__(self, *args, **kwargs):

            self.args = args
            self.kwargs = kwargs

    a_args = (0, 1, 2)
    b_args = (1, 2, 3)

    a_kwargs = {"arg": 0}
    b_kwargs = {"arg": 1}

    obj1 = _DummyMixinClasss(*a_args, **a_kwargs)
    obj2 = _DummyMixinClasss(*b_args, **b_kwargs)

    assert obj1.args == a_args == obj2.args
    assert obj1.kwargs == a_kwargs == obj2.kwargs
    assert obj1 is obj2
