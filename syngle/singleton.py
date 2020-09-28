"""This module includes the implementation of the Singleton class."""

from typing import Any, Optional


class Singleton(object):
    """Singleton class to extend to inherit the behaviour.

    Examples:
        To use it, simply extend the Singleton class.

        >>> from syngle import Singleton
        >>> class MyClass(Singleton): pass
        >>> myclass1 = MyClass()
        >>> myclass2 = MyClass()
        >>> myclass1 is myclass2
        True
    """

    _instance: Optional[Any] = None

    def __new__(cls, *args, **kwargs):
        """Creates a new instance or returns the instantiated one.

        Args:
            cls: class to instantiate
            *args: variable-length arguments
            **kwargs: key-word arguments

        Returns:
            Singleton: Unique instance of the object extending Singleton
        """
        if not isinstance(cls._instance, cls):

            cls._instance = object.__new__(cls, *args, **kwargs)

        return cls._instance
