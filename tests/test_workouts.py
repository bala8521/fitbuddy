import pytest


def test_generate_workout_plan_api(client):
    # 1. Create a user
    user_res = client.post("/api/users", json={
        "name": "Marcus Vance",
        "age": 31,
        "weight": 82.0,
        "goal": "Muscle Gain",
        "intensity": "High",
        "experience_level": "Intermediate"
    })
    assert user_res.status_code == 201
    user_id = user_res.json()["id"]

    # 2. Generate workout plan
    gen_res = client.post("/api/workouts/generate", json={"user_id": user_id})
    assert gen_res.status_code == 201
    plan = gen_res.json()

    assert plan["id"] is not None
    assert plan["user_id"] == user_id
    assert plan["goal"] == "Muscle Gain"
    assert plan["intensity"] == "High"
    assert plan["version"] == 1

    current_plan = plan["current_plan"]
    assert "days" in current_plan
    assert len(current_plan["days"]) == 7


def test_workout_has_exactly_seven_days(client):
    user_res = client.post("/api/users", json={
        "name": "Chloe Frazer",
        "age": 26,
        "weight": 61.0,
        "goal": "Weight Loss",
        "intensity": "Medium",
        "experience_level": "Beginner"
    })
    user_id = user_res.json()["id"]

    gen_res = client.post("/api/workouts/generate", json={"user_id": user_id})
    assert gen_res.status_code == 201
    plan_data = gen_res.json()["current_plan"]

    days = plan_data["days"]
    assert len(days) == 7

    for idx, day in enumerate(days, start=1):
        assert day["day"] == idx
        assert "focus" in day and len(day["focus"]) > 0
        assert "exercises" in day
        assert "cooldown" in day
        assert "recovery" in day
        # Ensure exercises contain structured fields
        for ex in day["exercises"]:
            assert "name" in ex and len(ex["name"]) > 0


def test_generate_workout_invalid_user(client):
    response = client.post("/api/workouts/generate", json={"user_id": 999999})
    assert response.status_code == 404


def test_get_workout_plan_by_id(client):
    user_res = client.post("/api/users", json={
        "name": "Nathan Drake",
        "age": 38,
        "weight": 78.0,
        "goal": "General Wellness",
        "intensity": "Low",
        "experience_level": "Beginner"
    })
    user_id = user_res.json()["id"]

    gen_res = client.post("/api/workouts/generate", json={"user_id": user_id})
    plan_id = gen_res.json()["id"]

    get_res = client.get(f"/api/workouts/{plan_id}")
    assert get_res.status_code == 200
    assert get_res.json()["id"] == plan_id
    assert get_res.json()["goal"] == "General Wellness"


def test_get_user_workouts_history(client):
    user_res = client.post("/api/users", json={
        "name": "Lara Croft",
        "age": 28,
        "weight": 57.0,
        "goal": "Muscle Gain",
        "intensity": "High",
        "experience_level": "Advanced"
    })
    user_id = user_res.json()["id"]

    # Generate 2 plans
    client.post("/api/workouts/generate", json={"user_id": user_id})
    client.post("/api/workouts/generate", json={"user_id": user_id})

    history_res = client.get(f"/api/workouts/user/{user_id}")
    assert history_res.status_code == 200
    plans = history_res.json()
    assert len(plans) >= 2


def test_workout_web_result_page(client):
    user_res = client.post("/api/users", json={
        "name": "Victor Sullivan",
        "age": 55,
        "weight": 85.0,
        "goal": "General Wellness",
        "intensity": "Low",
        "experience_level": "Beginner"
    })
    user_id = user_res.json()["id"]

    gen_res = client.post("/api/workouts/generate", json={"user_id": user_id})
    plan_id = gen_res.json()["id"]

    web_res = client.get(f"/workout/{plan_id}")
    assert web_res.status_code == 200
    assert "Victor Sullivan" in web_res.text
    assert "Day 1" in web_res.text
    assert "Day 7" in web_res.text
