"""This module includes the implementation of the Singleton metaclass."""

from typing import Any, Optional


class Singleton(type):
    """Singleton metaclass.

    Examples:
        To use it, simply extend the Singleton class.

        >>> from syngle import Singleton
        ...
        >>> class MyClass(metaclass=Singleton):
        ...     def __init__(self, *args, **kwargs):
        ...         pass
        ...
        >>> myclass1 = MyClass()
        >>> myclass2 = MyClass()
        ...
        >>> assert myclass1 is myclass2
    """

    _instance: Optional[Any] = None

    def __call__(cls, *args, **kwargs):
        """Creates a new instance or returns the instantiated one.

        Args:
            cls: class to instantiate
            *args: variable-length arguments
            **kwargs: key-word arguments

        Returns:
            Singleton: Unique instance of the object extending Singleton
        """
        if not isinstance(cls._instance, cls):

            cls._instance = super().__call__(*args, **kwargs)

        return cls._instance
