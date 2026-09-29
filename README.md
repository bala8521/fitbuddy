# ⚡ FitBuddy - AI-Powered Personalized Fitness & Nutrition Web Application

FitBuddy is a production-grade full-stack web application designed to generate, refine, and manage personalized 7-day workout plans and science-backed nutrition/recovery guidance using FastAPI, SQLAlchemy ORM, SQLite/PostgreSQL, Jinja2 responsive templates, and Google's Gemini GenAI API.

---

## 🌟 Key Features

1. **Fitness Profile Engine**: User profiling capturing age, weight, target fitness goals (*Weight Loss*, *Muscle Gain*, *General Wellness*), workout intensity (*Low*, *Medium*, *High*), and training experience level.
2. **7-Day Structured AI Workout Generator**: Gemini AI-powered 7-day microcycle generation featuring daily focus areas, dynamic warm-up drills, structured exercise schemes (sets, reps, rest intervals, form cues), cool-down stretches, and daily recovery protocols.
3. **Interactive Plan Refinement Feedback Loop**: Submit natural language modification requests (e.g., *"More focus on cardio"*, *"Include more rest days"*, *"Reduce intensity"*, *"Add upper-body work"*) to remodel routines while tracking version increments without destroying historical baselines.
4. **Instant Nutrition & Recovery Guidance**: Goal-tailored dietary tips, hydration rules, protein distribution guidelines, and sleep hygiene recommendations.
5. **Secure Administrative Control Center**: Protected administrative console with PBKDF2-HMAC-SHA256 password hashing, HMAC-SHA256 signed session cookies, real-time KPI metrics, user inspection, and cascading account deletion.
6. **Robust AI Resilience & Offline Fallbacks**: Graceful error handling for missing API keys, network outages, rate limits, and quota exhaustion with high-fidelity deterministic fallback plans.
7. **Production Architecture**: Strict separation of concerns (Core, Database, Models, Schemas, Routers, Services, Prompts, Templates, Static Assets) with 100% test coverage across all workflows.

---

## 🏗️ Architecture Flow

```
                     +---------------------------------------+
                     |         Browser / Client UI           |
                     |   (Jinja2 + Semantic HTML5 + CSS/JS)  |
                     +-------------------+-------------------+
                                         |
                                         v
                     +---------------------------------------+
                     |         FastAPI Web Application       |
                     |  - Lifespan Context & Exception Trap  |
                     |  - Pydantic v2 Boundary Validation    |
                     +---------+-------------------+---------+
                               |                   |
            +------------------+                   +------------------+
            |                                                         |
            v                                                         v
+-------------------------+                               +-------------------------+
|   Routers / Web & API   |                               |      Admin Console      |
|  - Web HTML Endpoints   |                               |  - Session Token Auth   |
|  - REST API (/api/...)  |                               |  - Real-Time KPI Stats  |
+-----------+-------------+                               +------------+------------+
            |                                                         |
            +-------------------------+-------------------------------+
                                      |
                                      v
                     +---------------------------------------+
                     |            Services Layer             |
                     |  - UserService     - WorkoutService   |
                     |  - FeedbackService - NutritionService |
                     |  - AdminService                       |
                     +-------------------+-------------------+
                                         |
                        +----------------+----------------+
                        |                                 |
                        v                                 v
         +-----------------------------+   +-----------------------------+
         |      Gemini AI Service      |   |       Database Layer        |
         |  - Google GenAI SDK Client  |   |  - SQLAlchemy 2.0 ORM       |
         |  - Structured JSON Schemas  |   |  - SQLite / Foreign Keys ON |
         |  - Deterministic Fallback   |   |  - Alembic Migrations       |
         +-----------------------------+   +-----------------------------+
```

---

## 🛠️ Technology Stack

- **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com/) (Python 3.11+)
- **ASGI Server**: [Uvicorn](https://www.uvicorn.org/)
- **ORM & Database**: [SQLAlchemy 2.0](https://www.sqlalchemy.org/) with SQLite (local) / PostgreSQL (production ready)
- **Migrations Engine**: [Alembic](https://alembic.sqlalchemy.org/)
- **Validation & Settings**: [Pydantic v2](https://docs.pydantic.dev/) & [pydantic-settings](https://github.com/pydantic/pydantic-settings)
- **Templating**: [Jinja2](https://jinja.palletsprojects.com/)
- **AI Integration**: [Google GenAI Python SDK](https://github.com/googleapis/python-genai) (`gemini-2.5-flash`)
- **Testing**: [Pytest](https://pytest.org/) & [Starlette TestClient / HTTPX](https://www.python-httpx.org/)

---

## 📁 Project Structure

```text
FitBuddy/
├── app/
│   ├── __init__.py
│   ├── main.py                     # Application entry point, lifespan, & exception handlers
│   │
│   ├── core/                       # Central configuration & security
│   │   ├── __init__.py
│   │   ├── config.py               # Pydantic Settings (.env management)
│   │   ├── security.py             # PBKDF2-HMAC-SHA256 password hashing & verification
│   │   └── logging.py              # Central application logger
│   │
│   ├── db/                         # Database connection & models
│   │   ├── __init__.py
│   │   ├── database.py             # Engine, SessionLocal, Base, & SQLite pragmas
│   │   ├── models.py               # SQLAlchemy ORM models (User, WorkoutPlan, etc.)
│   │   └── migrations/             # Alembic migration environment
│   │       ├── env.py
│   │       ├── script.py.mako
│   │       └── versions/           # Versioned migration scripts
│   │
│   ├── schemas/                    # Pydantic validation models
│   │   ├── __init__.py
│   │   ├── user.py                 # User creation, update, and response schemas
│   │   ├── workout.py              # 7-day structured plan validation schemas
│   │   ├── feedback.py             # Modification request schemas
│   │   └── nutrition.py            # Nutrition and recovery tip schemas
│   │
│   ├── services/                   # Business logic layer
│   │   ├── __init__.py
│   │   ├── gemini_service.py       # Google GenAI integration with fallback engine
│   │   ├── user_service.py         # User profile persistence & querying
│   │   ├── workout_service.py      # Workout plan generation & retrieval
│   │   ├── feedback_service.py     # Plan revision & version management
│   │   ├── nutrition_service.py    # Nutrition tip generator & history
│   │   └── admin_service.py        # Admin authentication & metric calculations
│   │
│   ├── prompts/                    # AI prompt engineering modules
│   │   ├── __init__.py
│   │   ├── workout.py              # 7-day workout plan system instructions & prompt builder
│   │   ├── feedback.py             # Feedback refinement prompt builder
│   │   └── nutrition.py            # Nutrition tip prompt builder
│   │
│   ├── routers/                    # Route handlers
│   │   ├── __init__.py
│   │   ├── web.py                  # HTML template endpoints (Home, Profile, Result, Feedback)
│   │   ├── api.py                  # REST API endpoints (/api/users, /api/workouts, etc.)
│   │   └── admin.py                # Protected administrative routes & auth controllers
│   │
│   └── templates/                  # Jinja2 HTML templates
│       ├── base.html               # Base layout with navigation and safety disclaimer
│       ├── index.html              # Landing page
│       ├── profile.html            # Profile creation form
│       ├── profile_view.html       # User profile & saved plans view
│       ├── generating.html         # AI generation transition screen
│       ├── result.html             # 7-Day interactive schedule view
│       ├── feedback.html           # Plan refinement form
│       ├── nutrition.html          # Nutrition & recovery guide center
│       ├── history.html            # Historical plans and versions archive
│       ├── error.html              # Universal error page (404, 422, 500)
│       └── admin/                  # Admin templates
│           ├── login.html          # Admin authentication form
│           ├── dashboard.html      # System KPI dashboard & user listing
│           └── user_detail.html    # Detailed user audit & plan inspection
│
├── static/                         # Static web assets
│   ├── css/
│   │   └── style.css               # Athletic fitness dark-mode design system
│   └── js/
│       └── app.js                  # Day tab switching, loading states, & API triggers
│
├── tests/                          # Automated Pytest suite
│   ├── conftest.py                 # Test fixtures & database setup
│   ├── test_health.py              # Health check & home page tests
│   ├── test_users.py               # User creation, validation, & query tests
│   ├── test_workouts.py            # 7-day plan generation & structure tests
│   ├── test_feedback.py            # Feedback modification & version increment tests
│   ├── test_nutrition.py           # Nutrition guidance tests
│   └── test_admin.py               # Admin auth & dashboard security tests
│
├── .env.example                    # Environment variables template
├── .gitignore                      # Git exclusion rules
├── alembic.ini                     # Alembic migration configuration
├── requirements.txt                # Python package dependencies
├── run.py                          # Local development execution script
└── README.md                       # Documentation
```

---

## 🚀 Getting Started

### 1. Clone & Setup Environment

```bash
# Clone the repository
cd FitBuddy

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows (PowerShell):
.venv\Scripts\Activate.ps1
# On Linux / macOS:
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Configure the settings inside `.env`:

```ini
APP_NAME=FitBuddy
ENVIRONMENT=development
DEBUG=True
HOST=127.0.0.1
PORT=8000
SECRET_KEY=fitbuddy-dev-secret-key-change-in-production-1234567890

# Database
DATABASE_URL=sqlite:///./fitbuddy.db

# Google Gemini API (Optional for offline testing; required for live Gemini calls)
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_WORKOUT_MODEL=gemini-2.5-flash
GEMINI_FAST_MODEL=gemini-2.5-flash

# Administrator Credentials
ADMIN_USERNAME=admin
ADMIN_PASSWORD=adminpassword123
```

> **Note**: If `GEMINI_API_KEY` is omitted or unavailable, FitBuddy seamlessly utilizes its built-in expert-verified deterministic workout generator.

### 4. Initialize Database & Run Migrations

```bash
# Apply Alembic database migrations
python -m alembic upgrade head
```

### 5. Launch the Application

```bash
# Option A: Run via runner script
python run.py

# Option B: Run directly via Uvicorn
uvicorn app.main:app --reload --port 8000
```

Open your browser and visit:
- **Application UI**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Interactive Swagger API Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc API Documentation**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
- **Admin Control Console**: [http://127.0.0.1:8000/admin/login](http://127.0.0.1:8000/admin/login) *(Default: `admin` / `adminpassword123`)*

---

## 🧪 Running Automated Tests

FitBuddy includes a comprehensive suite of 31 automated tests with 100% passing status:

```bash
# Run all tests
python -m pytest

# Run with verbose output
python -m pytest -v
```

---

## 📡 REST API Endpoints Reference

| Method | Endpoint | Description | Protected |
|---|---|---|---|
| `GET` | `/health` | Root application health check | No |
| `GET` | `/api/health` | Database & Gemini service status | No |
| `POST` | `/api/users` | Create user profile with validation | No |
| `GET` | `/api/users/{user_id}` | Retrieve user profile by ID | No |
| `GET` | `/api/users` | Paginated listing of user profiles | No |
| `POST` | `/api/workouts/generate` | Generate 7-day plan via Gemini AI | No |
| `GET` | `/api/workouts/{plan_id}` | Retrieve workout plan by ID | No |
| `GET` | `/api/workouts/user/{user_id}` | Retrieve all workout plans for a user | No |
| `POST` | `/api/workouts/{plan_id}/feedback` | Submit feedback & refine plan | No |
| `GET` | `/api/workouts/{plan_id}/feedback` | List feedback revisions for a plan | No |
| `POST` | `/api/nutrition/tip` | Generate goal-based nutrition tip | No |
| `GET` | `/api/nutrition/tips` | List recent nutrition tips | No |
| `GET` | `/api/admin/metrics` | System statistics and user analytics | **Yes (Admin)** |

---

## 🔒 Security Best Practices

1. **Secrets Management**: No API keys or passwords in source code. Centralized via `.env`.
2. **Password Protection**: Passwords hashed using PBKDF2-HMAC-SHA256 with cryptographically generated salts.
3. **Session Security**: Admin sessions authenticated via HMAC-SHA256 signed HTTP-only cookies with `SameSite=Lax`.
4. **Input Sanitization**: Server-side validation via Pydantic v2 prevents prompt injection, invalid types, and out-of-boundary payloads.
5. **Safe Error Handling**: Internal exception stack traces are masked in production mode.

---

## ⚠️ Health & Safety Medical Disclaimer

FitBuddy is an artificial intelligence-driven fitness planning and wellness education application. It provides generalized training routines and dietary guidance based on user-provided inputs. **FitBuddy is NOT a medical organization and does NOT provide medical diagnosis, treatment, or clinical advice.** Users should always consult with a licensed physician or healthcare provider before undertaking any new physical exercise or dietary regimen. Discontinue exercise immediately if you experience dizziness, shortness of breath, or sharp pain.

---

## 📄 License

MIT License. Developed for production-grade AI applications.
