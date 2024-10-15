"""conftest"""

import pytest
from fastapi.testclient import TestClient

from src.server import http


@pytest.fixture
def test_client():
    """test client"""
    return TestClient(http.app)
