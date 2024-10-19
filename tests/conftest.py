"""conftest"""

import pytest
from fastapi.testclient import TestClient

from service.server import http


@pytest.fixture
def test_client():
    """test client"""
    return TestClient(http.app)
