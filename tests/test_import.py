"""This module tests that imports work as expected."""

import importlib


def test_relative_import_singleton():
    """Tests that Singleton can be imported directly."""
    importlib.import_module("syngle", "Singleton")


def test_absolute_import_singleton():
    """Tests that Singleton can be imported explicitly."""
    importlib.import_module("syngle.singleton", "Singleton")
