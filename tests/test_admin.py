import pytest
from app.core.config import get_settings

settings = get_settings()


def test_admin_dashboard_unauthenticated_redirect(client):
    response = client.get("/admin/dashboard", follow_redirects=False)
    # Expect redirect to /admin/login
    assert response.status_code == 303
    assert "/admin/login" in response.headers.get("location", "")


def test_admin_metrics_unauthenticated_forbidden(client):
    response = client.get("/api/admin/metrics", follow_redirects=False)
    assert response.status_code == 303 or response.status_code == 401 or response.status_code == 403


def test_admin_login_invalid_password(client):
    response = client.post("/admin/login", data={
        "username": settings.ADMIN_USERNAME,
        "password": "wrongpassword123"
    })
    assert response.status_code == 401
    assert "Invalid username or password" in response.text


def test_admin_login_success_and_dashboard_access(client):
    # 1. Login with valid credentials
    login_res = client.post("/admin/login", data={
        "username": settings.ADMIN_USERNAME,
        "password": settings.ADMIN_PASSWORD
    }, follow_redirects=False)

    assert login_res.status_code == 303
    assert "fitbuddy_admin_token" in login_res.cookies

    # 2. Access dashboard with the session cookie
    dash_res = client.get("/admin/dashboard", cookies=login_res.cookies)
    assert dash_res.status_code == 200
    assert "Admin Control Center" in dash_res.text
    assert "Total Users" in dash_res.text


def test_admin_inspect_and_delete_user(client):
    # Login first
    login_res = client.post("/admin/login", data={
        "username": settings.ADMIN_USERNAME,
        "password": settings.ADMIN_PASSWORD
    })
    cookies = login_res.cookies

    # Create a user to test admin operations
    user_res = client.post("/api/users", json={
        "name": "Admin Test Subject",
        "age": 22,
        "weight": 70.0,
        "goal": "Weight Loss",
        "intensity": "Medium",
        "experience_level": "Beginner"
    })
    user_id = user_res.json()["id"]

    # Inspect user
    inspect_res = client.get(f"/admin/users/{user_id}", cookies=cookies)
    assert inspect_res.status_code == 200
    assert "Admin Test Subject" in inspect_res.text

    # Delete user
    delete_res = client.post(f"/admin/users/{user_id}/delete", cookies=cookies, follow_redirects=False)
    assert delete_res.status_code == 303

    # Verify user is deleted
    get_res = client.get(f"/api/users/{user_id}")
    assert get_res.status_code == 404


def test_admin_logout(client):
    login_res = client.post("/admin/login", data={
        "username": settings.ADMIN_USERNAME,
        "password": settings.ADMIN_PASSWORD
    })
    cookies = login_res.cookies

    logout_res = client.get("/admin/logout", cookies=cookies, follow_redirects=False)
    assert logout_res.status_code == 303
    assert "/admin/login" in logout_res.headers.get("location", "")
