"""This module includes the implementation of the singleton decorator."""

import functools
from typing import Any


def singleton(cls):
    """Singleton decorator.

    Args:
        cls: class to decorate

    Returns:
        Callable[([_Any_Callable], _Any_Callable)]: Decorated class implementing the Singleton pattern

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
        >>> assert myclass1 is myclass2
    """

    @functools.wraps(cls)
    def wrapper(*args, **kwargs) -> Any:
        """Wrapper function implementing the singleton pattern.

        Args:
            *args: variable-length arguments
            **kwargs: key-word arguments

        Returns:
            Any: single instance of the class
        """
        if wrapper._instance is None:

            wrapper._instance = cls(*args, **kwargs)

        return wrapper._instance

    wrapper._instance = None

    return wrapper
