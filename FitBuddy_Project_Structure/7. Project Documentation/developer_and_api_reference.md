# Phase 7: Project Documentation - Developer Onboarding & API Reference

## 1. Developer Quick Start

### 1. Repository Setup
```bash
# Clone the repository
cd FitBuddy

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1   # Windows PowerShell
# source .venv/bin/activate  # Linux / macOS

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure `.env`
Create `.env` based on `.env.example`:
```ini
APP_NAME=FitBuddy
ENVIRONMENT=development
DEBUG=True
HOST=127.0.0.1
PORT=8000
SECRET_KEY=fitbuddy-dev-secret-key-change-in-production-1234567890
DATABASE_URL=sqlite:///./fitbuddy.db
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_WORKOUT_MODEL=gemini-2.5-flash
ADMIN_USERNAME=admin
ADMIN_PASSWORD=adminpassword123
```

### 3. Run Database Migrations & Launch Dev Server
```bash
python -m alembic upgrade head
python run.py
```

---

## 2. Interactive API Documentation

FitBuddy provides automated, interactive OpenAPI and ReDoc documentation:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc UI**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
- **OpenAPI Schema JSON**: [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

---

## 3. Running Automated Tests & Linter
```bash
# Run full Pytest suite
python -m pytest -v

# Run with test coverage report
python -m pytest --cov=app tests/
```
