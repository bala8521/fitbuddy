# Phase 5: Project Development Phase - Backend Architecture & Modules

## 1. Modular Directory Structure

The backend is organized with a strict separation of concerns:

```text
app/
├── main.py                     # App lifespan, global middleware & exception handlers
├── core/
│   ├── config.py               # Pydantic Settings (.env configuration)
│   ├── security.py             # PBKDF2-HMAC-SHA256 & HMAC cookie signing
│   └── logging.py              # Central application logger
├── db/
│   ├── database.py             # SQLAlchemy Engine, SessionLocal, & base setup
│   ├── models.py               # Declarative ORM models
│   └── migrations/             # Alembic migration environment
├── schemas/
│   ├── user.py                 # User creation, update, and response schemas
│   ├── workout.py              # 7-Day workout plan Pydantic schemas
│   ├── feedback.py             # Plan refinement request schemas
│   └── nutrition.py            # Nutrition tip schemas
├── services/
│   ├── gemini_service.py       # Google GenAI SDK client & fallback engine
│   ├── user_service.py         # User CRUD & querying
│   ├── workout_service.py      # Workout plan generation & persistence
│   ├── feedback_service.py     # Plan revision & versioning
│   ├── nutrition_service.py    # Nutrition tip generator
│   └── admin_service.py        # Admin auth & KPI metrics
├── prompts/
│   ├── workout.py              # 7-Day workout prompt templates
│   ├── feedback.py             # Plan modification prompts
│   └── nutrition.py            # Nutrition tip prompts
└── routers/
    ├── web.py                  # HTML template route handlers
    ├── api.py                  # REST API JSON route handlers
    └── admin.py                # Admin console route handlers
```

---

## 2. Core Service Implementations

### 1. `app/core/config.py`
Centralizes all application configurations via `pydantic-settings`. Automatically loads environment variables from `.env` with fallback defaults:
- `APP_NAME`: `FitBuddy`
- `DATABASE_URL`: `sqlite:///./fitbuddy.db`
- `GEMINI_API_KEY`: Google GenAI API key
- `GEMINI_WORKOUT_MODEL`: `gemini-2.5-flash`
- `ADMIN_USERNAME` & `ADMIN_PASSWORD`: Admin credentials
- `SECRET_KEY`: Cryptographic signing key

### 2. `app/core/security.py`
Implements cryptographically robust authentication primitives:
- `hash_password(password: str) -> str`: Uses `hashlib.pbkdf2_hmac` with `sha256`, 100,000 iterations, and a randomly generated 16-byte salt.
- `verify_password(password: str, hashed: str) -> bool`: Constant-time comparison using `secrets.compare_digest`.
- `sign_session_cookie(data: dict) -> str`: Signs session payloads using `hmac.new(..., hashlib.sha256)`.
- `verify_session_cookie(cookie: str) -> Optional[dict]`: Verifies signature integrity and expiration.

### 3. `app/services/workout_service.py`
Coordinates the workout generation workflow:
1. Validates user existence via `UserService`.
2. Assembles user parameters into structured prompt definitions.
3. Invokes `GeminiService.generate_workout_plan(user)`.
4. Parses resulting structured JSON into Pydantic models.
5. Persists the `WorkoutPlan`, 7 `DailyWorkout` records, and 20+ `Exercise` records inside a single atomic database transaction.
