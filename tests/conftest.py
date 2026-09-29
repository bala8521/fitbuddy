import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db.database import init_db


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """Initializes database schema once for test sessions."""
    init_db()


@pytest.fixture
def client():
    """Provides test client."""
    with TestClient(app) as test_client:
        yield test_client
