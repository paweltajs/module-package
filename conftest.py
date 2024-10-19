"""Pytest configuration file."""

import os.path

import pytest


@pytest.fixture(scope="session", autouse=True)
def testing_context(tmp_path_factory):
    """Pytest general context."""
    tc = {
        "output_dir": f"{tmp_path_factory.mktemp('out')}".replace("\\", "/"),
        "resources_dir": f"{os.getcwd()}/resources".replace("\\", "/")
    }
    yield tc
