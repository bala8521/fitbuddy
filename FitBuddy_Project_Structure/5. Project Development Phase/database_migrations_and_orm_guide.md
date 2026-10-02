# Phase 5: Project Development Phase - Database Migrations & ORM Implementation Guide

## 1. SQLAlchemy 2.0 Engine & Connection Setup

In `app/db/database.py`, database connectivity is initialized with connection pooling and dialect-specific pragmas:

```python
from sqlalchemy import create_engine, event
from sqlalchemy.orm import declarative_base, sessionmaker
from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {}
)

# Enable Foreign Key enforcement for SQLite
@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if "sqlite" in settings.DATABASE_URL:
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
```

---

## 2. Alembic Migration Workflow

Database schema evolution is managed through **Alembic**:

### Configuration (`alembic.ini` & `app/db/migrations/env.py`)
In `env.py`, `target_metadata` imports `Base.metadata` from `app.db.models`:

```python
from app.db.database import Base
from app.db import models  # Ensures all ORM models are registered

target_metadata = Base.metadata
```

### Common Migration Commands:

```bash
# Generate a new migration script following model changes
alembic revision --autogenerate -m "Add nutrition and feedback tables"

# Apply all pending migrations to the database
alembic upgrade head

# Rollback the last migration
alembic downgrade -1
```

---

## 3. Dependency Injection in FastAPI

Database sessions are injected into FastAPI endpoints using a safe context manager pattern ensuring connections are automatically closed and recycled:

```python
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```
