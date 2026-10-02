# Phase 4: Project Planning Phase - Tech Stack & Resource Allocation

## 1. Technology Selection & Architectural Justification

| Layer | Selected Technology | Alternative Evaluated | Justification & Technical Advantages |
|---|---|---|---|
| **Backend Framework** | **FastAPI** | Flask, Django | High-performance asynchronous execution, native Pydantic v2 data validation, automated OpenAPI documentation generation, lightweight memory footprint. |
| **AI LLM Engine** | **Google Gemini 2.5 Flash** | OpenAI GPT-4o-mini | Ultra-fast inference latency (<1.5s), cost-effective high-token throughput, native JSON structured schema output support via Google GenAI SDK. |
| **ORM & Persistence** | **SQLAlchemy 2.0** | Raw SQL, Peewee | Industry-standard ORM with full type hinting, declarative base mappings, powerful relationship cascades, and zero-downtime Alembic migration support. |
| **Database** | **SQLite (Dev) / PostgreSQL (Prod)** | MongoDB, DynamoDB | Strict ACID transaction guarantees, normalized relational integrity across users, plans, days, and exercises. |
| **Frontend Architecture** | **Jinja2 + Vanilla CSS + JS** | React / Vue SPA | Zero build step complexity, instant server-side page loads, enhanced SEO, unified Python deployment, and lightweight bundle size. |
| **Testing Suite** | **Pytest + HTTPX** | Unittest | Concise fixture management, parameterized test execution, asynchronous client testing support, comprehensive coverage reporting. |

---

## 2. Resource & Team Role Allocation

```
+--------------------------------------------------------------------------+
|                     FITBUDDY PROJECT RESOURCE ALLOCATION                 |
+--------------------------+-----------------------------------------------+
| Role                     | Key Responsibilities                          |
+--------------------------+-----------------------------------------------+
| Backend & AI Engineer    | FastAPI routes, Gemini GenAI client, fallback |
|                          | engine, Pydantic schemas, ORM queries.        |
+--------------------------+-----------------------------------------------+
| Frontend & UI/UX Dev     | Athletic dark-mode design system, Jinja2      |
|                          | templates, responsive microcycle tab switcher.|
+--------------------------+-----------------------------------------------+
| Database Administrator   | Database schema design, ER models, Alembic    |
|                          | migrations, indexing, SQLite pragma setup.    |
+--------------------------+-----------------------------------------------+
| QA & Security Specialist | Pytest suite design (31 tests), auth audit,   |
|                          | cookie signing verification, boundary tests.  |
+--------------------------+-----------------------------------------------+
```
