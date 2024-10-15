"""issues router tests"""

from fastapi.testclient import TestClient


def test_create_issue(test_client: TestClient):
    """test create issue"""
    response = test_client.post("/api/v1/issues/issues", json={"title": "test"})
    json_response = response.json()

    assert response.status_code == 200
    assert json_response.get("title") == "test"
    assert json_response.get("id")


def test_get_issues(test_client: TestClient):
    """test get issues"""
    response = test_client.get("/api/v1/issues/issues")

    assert response.status_code == 200
    assert response.json() == []


def test_get_issue(test_client: TestClient):
    """test get issue"""
    response = test_client.get("/api/v1/issues/issues/1")

    assert response.status_code == 200
    assert response.json() == {"id": 1}


def test_update_issue(test_client: TestClient):
    """test update issue"""
    response = test_client.patch("/api/v1/issues/issues/1", json={})

    assert response.status_code == 200
    assert response.json() == {"id": 1}

    response = test_client.patch("/api/v1/issues/issues/1", json={"title": "test"})

    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "test"}


def test_delete_issue(test_client: TestClient):
    """test delete issue"""
    response = test_client.delete("/api/v1/issues/issues/2")

    assert response.status_code == 200
    assert response.json() == {"id": 2}
