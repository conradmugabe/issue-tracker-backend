"""issues router tests"""

from fastapi.testclient import TestClient

ISSUES_ENDPOINT = "/api/v1/issues"


def test_create_issue(test_client: TestClient):
    """test create issue"""
    response = test_client.post(f"{ISSUES_ENDPOINT}", json={"title": "test"})
    json_response = response.json()

    assert response.status_code == 200
    assert json_response.get("title") == "test"
    assert json_response.get("id")


def test_get_issues(test_client: TestClient):
    """test get issues"""
    response = test_client.get(f"{ISSUES_ENDPOINT}")

    assert response.status_code == 200
    assert response.json() == []


def test_get_issue_fail_404(test_client: TestClient):
    """test get issue"""
    response = test_client.get(f"{ISSUES_ENDPOINT}/1")

    assert response.status_code == 404
    assert response.json() == {"detail": "Not found"}


def test_get_issue_success(test_client: TestClient):
    """test get issue"""
    response = test_client.post(f"{ISSUES_ENDPOINT}", json={"title": "test 1"})
    issue = response.json()
    issue_id = issue.get("id")

    response = test_client.get(f"{ISSUES_ENDPOINT}/{issue_id}")

    assert response.status_code == 200
    assert response.json() == issue


def test_update_issue(test_client: TestClient):
    """test update issue"""
    response = test_client.patch(f"{ISSUES_ENDPOINT}/1", json={})

    assert response.status_code == 200
    assert response.json() == {"id": 1}

    response = test_client.patch(f"{ISSUES_ENDPOINT}/1", json={"title": "test"})

    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "test"}


def test_delete_issue_fail_404(test_client: TestClient):
    """test delete issue"""
    response = test_client.delete(f"{ISSUES_ENDPOINT}/2")

    assert response.status_code == 404
    assert response.json() == {"detail": "Not found"}


def test_delete_issue_success(test_client: TestClient):
    """test delete issue success"""
    response = test_client.post(f"{ISSUES_ENDPOINT}", json={"title": "test 1"})
    issue = response.json()
    issue_id = issue.get("id")

    response = test_client.delete(f"{ISSUES_ENDPOINT}/{issue_id}")
    assert response.status_code == 200
    assert response.json() == issue

    response = test_client.delete(f"{ISSUES_ENDPOINT}/{issue_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not found"}
