import pytest

from api.client import JsonPlaceholderClient


@pytest.fixture(scope="session")
def client():
    return JsonPlaceholderClient()