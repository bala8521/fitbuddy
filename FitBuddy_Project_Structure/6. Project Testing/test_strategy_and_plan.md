# Phase 6: Project Testing - Test Strategy & Test Plan

## 1. Testing Strategy Overview

The testing strategy for FitBuddy adopts a rigorous quality assurance methodology combining automated unit tests, integration tests, mock Gemini AI verifications, end-to-end HTTP endpoint tests, and security boundary audits.

---

## 2. Test Pyramid & Scope

```
             / \
            /   \      E2E Web View Tests (Starlette / Jinja2 HTML)
           /-----\
          /       \     Integration API Tests (REST Endpoints + DB)
         /---------\
        /           \    Unit Tests & Mocked AI Service Tests
       /-------------\
```

### Scope:
1. **Health & Connectivity Tests**: Verify root application health, database readiness, and config validity.
2. **User Profile Tests**: Boundary tests for age limits, weight ranges, enum goals, and persistence.
3. **Workout Generation Tests**: Verify 7-day microcycle generation, correct JSON parsing, fallback triggers, and relational foreign keys.
4. **Feedback Loop Tests**: Test version incrementation (`v1.0 -> v2.0`), feedback history records, and plan remodeling.
5. **Nutrition & Recovery Tests**: Validate goal-aligned nutrition tip generation and retrieval.
6. **Admin Security & Auth Tests**: Validate PBKDF2 password verification, HMAC cookie forgery rejection, protected route redirects, and metric calculations.

---

## 3. Test Fixture Configuration (`tests/conftest.py`)

Tests run against an in-memory SQLite database isolated from production data:

```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from app.main import app
from app.db.database import Base, get_db

TEST_DATABASE_URL = "sqlite:///:memory:"

@pytest.fixture(scope="function")
def db_session():
    engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()
```
