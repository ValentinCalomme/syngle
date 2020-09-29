"""This module tests that imports work as expected."""

import importlib


def test_relative_import_decorator():
    """Tests that Singleton can be imported directly."""
    importlib.import_module("syngle", "singleton")


def test_absolute_import_decorator():
    """Tests that singleton can be imported explicitly."""
    importlib.import_module("syngle.decorator", "singleton")
