import pytest


def test_create_user_api(client):
    payload = {
        "name": "Sarah Connor",
        "age": 29,
        "weight": 65.5,
        "goal": "Muscle Gain",
        "intensity": "High",
        "experience_level": "Intermediate"
    }
    response = client.post("/api/users", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] is not None
    assert data["name"] == "Sarah Connor"
    assert data["goal"] == "Muscle Gain"
    assert data["intensity"] == "High"


def test_create_user_invalid_age(client):
    payload = {
        "name": "Invalid Young",
        "age": 5,  # Below minimum allowed age of 12
        "weight": 50.0,
        "goal": "Weight Loss",
        "intensity": "Medium",
        "experience_level": "Beginner"
    }
    response = client.post("/api/users", json=payload)
    assert response.status_code == 422


def test_create_user_invalid_weight(client):
    payload = {
        "name": "Invalid Weight",
        "age": 25,
        "weight": 500.0,  # Exceeds max weight of 400kg
        "goal": "General Wellness",
        "intensity": "Low",
        "experience_level": "Beginner"
    }
    response = client.post("/api/users", json=payload)
    assert response.status_code == 422


def test_get_user_by_id(client):
    create_res = client.post("/api/users", json={
        "name": "John Doe",
        "age": 35,
        "weight": 80.0,
        "goal": "Weight Loss",
        "intensity": "Medium",
        "experience_level": "Beginner"
    })
    user_id = create_res.json()["id"]

    get_res = client.get(f"/api/users/{user_id}")
    assert get_res.status_code == 200
    assert get_res.json()["name"] == "John Doe"


def test_get_nonexistent_user(client):
    response = client.get("/api/users/999999")
    assert response.status_code == 404


def test_profile_web_form_submission(client):
    form_data = {
        "name": "Elena Fisher",
        "age": "27",
        "weight": "58.0",
        "goal": "General Wellness",
        "intensity": "Low",
        "experience_level": "Beginner"
    }
    response = client.post("/profile", data=form_data, follow_redirects=True)
    assert response.status_code == 200
    assert "Elena Fisher" in response.text
