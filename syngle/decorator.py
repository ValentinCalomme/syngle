"""This module includes the implementation of the singleton decorator."""

import functools


def singleton(cls):
    """Singleton decorator.

    Examples:
        >>> from syngle import singleton
        ...
        >>> @singleton
        ... class MyClass:
        ...     def __init__(self, *args, **kwargs):
        ...         pass
        ...
        >>> myclass1 = MyClass()
        >>> myclass2 = MyClass()
        ...
        >>> myclass1 is myclass2
        True

    Args:
        cls: class to decorate

    Returns:
        Callable[([_Any_Callable], _Any_Callable)]: Decorated class implementing the Singleton pattern
    """

    @functools.wraps(cls)
    def wrapper(*args, **kwargs):

        if wrapper._instance is None:

            wrapper._instance = cls(*args, **kwargs)

        return wrapper._instance

    wrapper._instance = None

    return wrapper
