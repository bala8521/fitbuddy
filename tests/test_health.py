def test_root_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_api_health(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] in ["ok", "degraded"]
    assert "database" in data


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "FitBuddy" in response.text
