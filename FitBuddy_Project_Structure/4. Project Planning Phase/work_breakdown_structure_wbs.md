# Phase 4: Project Planning Phase - Work Breakdown Structure (WBS)

## 1. WBS Tree Hierarchy

```
1.0 FitBuddy Application System
├── 1.1 Core Backend & Configuration
│   ├── 1.1.1 Environment variables loader (Pydantic Settings)
│   ├── 1.1.2 Security utilities (PBKDF2 Hashing, HMAC Cookie Signing)
│   └── 1.1.3 Structured logging & exception middleware
│
├── 1.2 Database & Data Persistence
│   ├── 1.2.1 SQLAlchemy 2.0 ORM Entity modeling
│   ├── 1.2.2 SQLite foreign key pragma configuration
│   ├── 1.2.3 Alembic schema migration versioning
│   └── 1.2.4 Database repository & session dependency injection
│
├── 1.3 AI Intelligence & Prompt Engineering
│   ├── 1.3.1 Google GenAI Python SDK client initialization
│   ├── 1.3.2 7-Day workout generation system prompt & JSON schema
│   ├── 1.3.3 Feedback remodeling prompt design
│   ├── 1.3.4 Deterministic fallback generation engine
│   └── 1.3.5 Goal-specific nutrition recommendation generator
│
├── 1.4 Business Logic Services
│   ├── 1.4.1 UserService (CRUD, validation, indexing)
│   ├── 1.4.2 WorkoutService (AI dispatch, payload parsing, DB normalization)
│   ├── 1.4.3 FeedbackService (Plan revision, version incrementation)
│   ├── 1.4.4 NutritionService (Dietary tips, hydration rules)
│   └── 1.4.5 AdminService (Metrics calculation, auth checks, deletion)
│
├── 1.5 Presentation & Web Routers
│   ├── 1.5.1 HTML Web Router (Jinja2 view rendering)
│   ├── 1.5.2 REST API Router (JSON endpoints for external clients)
│   └── 1.5.3 Admin Portal Router (Session validation & dashboard)
│
├── 1.6 Frontend UI & Assets
│   ├── 1.6.1 Base Jinja2 layout & navigation
│   ├── 1.6.2 Athletic dark-mode CSS design system
│   ├── 1.6.3 Interactive microcycle tab switcher JavaScript
│   └── 1.6.4 Plan refinement modal & loading transition animations
│
├── 1.7 Quality Assurance & Automated Testing
│   ├── 1.7.1 Test database fixtures & Starlette TestClient setup
│   ├── 1.7.2 User profile validation test suite
│   ├── 1.7.3 7-Day workout generation & schema test suite
│   ├── 1.7.4 Feedback revision & version increment test suite
│   ├── 1.7.5 Nutrition & recovery test suite
│   └── 1.7.6 Admin authentication & dashboard security test suite
│
└── 1.8 Documentation & Release
    ├── 1.8.1 Complete 8-phase project lifecycle documentation
    ├── 1.8.2 User and Administrator operation manuals
    └── 1.8.3 Demonstration script & UI showcase
```
