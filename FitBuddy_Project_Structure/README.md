# FitBuddy - Project Lifecycle & Architecture Structure

Welcome to the comprehensive project lifecycle documentation for **FitBuddy: AI-Powered Personalized Fitness & Nutrition Web Application**.

This directory documents the complete software engineering lifecycle of the FitBuddy application across 8 distinct phases, from initial brainstorming to development, testing, and final demonstration.

---

## 📂 Project Directory Structure

```text
FitBuddy_Project_Structure/
├── 1. Brainstorming & Ideation/
│   ├── problem_statement_and_vision.md
│   ├── target_audience_and_personas.md
│   └── feature_brainstorming_and_matrix.md
│
├── 2. Requirement Analysis/
│   ├── functional_requirements.md
│   ├── non_functional_requirements.md
│   ├── use_case_specifications.md
│   └── system_constraints_and_assumptions.md
│
├── 3. Project Design Phase/
│   ├── system_architecture_design.md
│   ├── database_schema_and_er_diagram.md
│   ├── api_design_specification.md
│   └── ui_ux_wireframes_and_flow.md
│
├── 4. Project Planning Phase/
│   ├── project_roadmap_and_sprints.md
│   ├── work_breakdown_structure_wbs.md
│   ├── risk_management_and_mitigation.md
│   └── resource_and_tech_stack_allocation.md
│
├── 5. Project Development Phase/
│   ├── backend_architecture_and_modules.md
│   ├── ai_prompt_engineering_and_gemini_integration.md
│   ├── database_migrations_and_orm_guide.md
│   └── frontend_and_templating_implementation.md
│
├── 6. Project Testing/
│   ├── test_strategy_and_plan.md
│   ├── test_cases_and_matrix.md
│   ├── test_execution_and_results_report.md
│   └── security_and_performance_audit.md
│
├── 7. Project Documentation/
│   ├── user_manual_and_guide.md
│   ├── administrator_guide.md
│   ├── developer_and_api_reference.md
│   └── deployment_and_devops_guide.md
│
├── 8. Project Demonstration/
│   ├── project_demo_script_and_walkthrough.md
│   ├── system_screenshots_and_ui_showcase.md
│   └── project_deliverables_and_presentation_summary.md
│
└── README.md
```

---

## 🚀 Lifecycle Navigation & Phase Breakdown

| Phase | Directory | Description & Key Artifacts |
|---|---|---|
| **Phase 1** | [1. Brainstorming & Ideation](./1.%20Brainstorming%20%26%20Ideation/) | Problem statements, market opportunities, user personas, MoSCoW feature matrix, and product vision. |
| **Phase 2** | [2. Requirement Analysis](./2.%20Requirement%20Analysis/) | Functional and non-functional requirements (NFRs), detailed use-case specifications, system constraints, and medical disclaimers. |
| **Phase 3** | [3. Project Design Phase](./3.%20Project%20Design%20Phase/) | System architecture diagrams, database ER schemas, REST API specs, UI wireframes, and dark-mode athletic UX flow. |
| **Phase 4** | [4. Project Planning Phase](./4.%20Project%20Planning%20Phase/) | Agile sprint roadmaps, Work Breakdown Structure (WBS), risk mitigation matrix, and technology justification. |
| **Phase 5** | [5. Project Development Phase](./5.%20Project%20Development%20Phase/) | FastAPI backend architecture, Google Gemini 2.5 Flash prompt engineering, fallback engine, and Jinja2 frontend components. |
| **Phase 6** | [6. Project Testing](./6.%20Project%20Testing/) | Pytest test strategy, test matrix (31 test cases), execution logs, 100% pass verification, and security audits. |
| **Phase 7** | [7. Project Documentation](./7.%20Project%20Documentation/) | Complete User Manual, Administrator Operations Guide, Developer & API Reference, and DevOps Deployment Guide. |
| **Phase 8** | [8. Project Demonstration](./8.%20Project%20Demonstration/) | Live demo walkthrough script, UI screenshots breakdown, executive presentation summary, and future roadmap. |

---

## ⚡ Application Overview

- **Core Framework**: FastAPI (Python 3.11+) + SQLAlchemy 2.0 ORM
- **AI Intelligence**: Google Gemini 2.5 Flash GenAI API (`gemini-2.5-flash`) with structured JSON schema enforcement and zero-downtime deterministic fallback engine.
- **Frontend**: Jinja2 responsive templates, Vanilla CSS athletic dark-mode styling, dynamic vanilla JavaScript microcycle tab controller.
- **Data Persistence**: SQLite (local dev) / PostgreSQL (production) with Alembic migration version control.
- **Security**: PBKDF2-HMAC-SHA256 password hashing, HMAC-SHA256 signed session cookies, Pydantic v2 input boundary validation.
