import pytest


def test_nutrition_tip_api_general_wellness(client):
    payload = {
        "goal": "General Wellness"
    }
    response = client.post("/api/nutrition/tip", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["goal"] == "General Wellness"
    assert "tip" in data and len(data["tip"]) > 10


def test_nutrition_tip_api_muscle_gain(client):
    payload = {
        "goal": "Muscle Gain"
    }
    response = client.post("/api/nutrition/tip", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["goal"] == "Muscle Gain"
    assert "protein" in data["tip"].lower() or "surplus" in data["tip"].lower() or "sleep" in data["tip"].lower()


def test_nutrition_tip_api_weight_loss(client):
    payload = {
        "goal": "Weight Loss"
    }
    response = client.post("/api/nutrition/tip", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["goal"] == "Weight Loss"
    assert len(data["tip"]) > 10


def test_list_nutrition_tips(client):
    # Request a tip
    client.post("/api/nutrition/tip", json={"goal": "Weight Loss"})
    
    list_res = client.get("/api/nutrition/tips")
    assert list_res.status_code == 200
    tips = list_res.json()
    assert isinstance(tips, list)
    assert len(tips) >= 1


def test_nutrition_web_page(client):
    response = client.get("/nutrition")
    assert response.status_code == 200
    assert "AI Nutrition & Recovery Guide" in response.text
    assert "Protein Distribution" in response.text
