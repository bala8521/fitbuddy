import pytest


def test_submit_feedback_and_refine_plan(client):
    # 1. Create User
    user_res = client.post("/api/users", json={
        "name": "Sam Fisher",
        "age": 42,
        "weight": 83.0,
        "goal": "Muscle Gain",
        "intensity": "High",
        "experience_level": "Advanced"
    })
    user_id = user_res.json()["id"]

    # 2. Generate initial plan (v1)
    gen_res = client.post("/api/workouts/generate", json={"user_id": user_id})
    plan_id = gen_res.json()["id"]
    assert gen_res.json()["version"] == 1
    original_plan_title = gen_res.json()["current_plan"]["title"]

    # 3. Submit feedback: "More focus on cardio"
    fb_res = client.post(f"/api/workouts/{plan_id}/feedback", json={
        "feedback": "Please add more focus on cardiovascular endurance and HIIT finishers."
    })
    assert fb_res.status_code == 200
    updated_plan = fb_res.json()

    assert updated_plan["id"] == plan_id
    assert updated_plan["version"] == 2
    assert "summary" in updated_plan["current_plan"]
    assert len(updated_plan["current_plan"]["days"]) == 7

    # 4. Check feedback history endpoint
    history_res = client.get(f"/api/workouts/{plan_id}/feedback")
    assert history_res.status_code == 200
    feedbacks = history_res.json()
    assert len(feedbacks) == 1
    assert "cardiovascular" in feedbacks[0]["feedback"].lower()


def test_submit_empty_feedback_rejected(client):
    # Try sending empty feedback
    response = client.post("/api/workouts/1/feedback", json={
        "feedback": "   "
    })
    assert response.status_code == 422


def test_feedback_nonexistent_plan(client):
    response = client.post("/api/workouts/999999/feedback", json={
        "feedback": "Make it harder please."
    })
    assert response.status_code == 400 or response.status_code == 404


def test_feedback_web_form_submission(client):
    user_res = client.post("/api/users", json={
        "name": "Jill Valentine",
        "age": 30,
        "weight": 59.0,
        "goal": "Weight Loss",
        "intensity": "Medium",
        "experience_level": "Intermediate"
    })
    user_id = user_res.json()["id"]

    gen_res = client.post("/api/workouts/generate", json={"user_id": user_id})
    plan_id = gen_res.json()["id"]

    form_res = client.post(f"/workout/{plan_id}/feedback", data={
        "feedback": "Include more rest days for recovery."
    }, follow_redirects=True)
    assert form_res.status_code == 200
    assert "Jill Valentine" in form_res.text
    assert "Version 2" in form_res.text


def test_history_web_page(client):
    user_res = client.post("/api/users", json={
        "name": "Leon Kennedy",
        "age": 33,
        "weight": 79.0,
        "goal": "General Wellness",
        "intensity": "Medium",
        "experience_level": "Intermediate"
    })
    user_id = user_res.json()["id"]

    client.post("/api/workouts/generate", json={"user_id": user_id})

    history_page_res = client.get(f"/history/{user_id}")
    assert history_page_res.status_code == 200
    assert "Leon Kennedy" in history_page_res.text
    assert "Plan #" in history_page_res.text
