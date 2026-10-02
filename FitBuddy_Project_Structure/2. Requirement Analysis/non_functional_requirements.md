# Phase 2: Requirement Analysis - Non-Functional Requirements (NFRs)

## 1. Overview

Non-functional requirements define the quality attributes, constraints, performance benchmarks, and security safeguards of the FitBuddy platform.

---

## 2. Detailed NFR Specifications

### 1. Performance & Latency
- **NFR-P1 (UI Response Time)**: Static pages and cached template renders must complete in less than **100 milliseconds**.
- **NFR-P2 (AI Generation Latency)**: Gemini AI plan generation and schema parsing must complete in less than **3.5 seconds** under normal network conditions.
- **NFR-P3 (Fallback Execution Speed)**: Deterministic offline workout generation must execute in less than **50 milliseconds**.
- **NFR-P4 (Database Query Efficiency)**: Standard single-record retrieval operations (`SELECT by ID`) must execute in under **5 milliseconds** with proper index utilization.

---

### 2. Security & Data Protection
- **NFR-S1 (Secrets Segregation)**: All API keys, environment credentials, and secret keys must be loaded strictly from `.env` files via Pydantic Settings and never hardcoded in source code.
- **NFR-S2 (Credential Hashing)**: Passwords must be hashed using `PBKDF2-HMAC-SHA256` with randomly generated salt strings (minimum 100,000 iterations).
- **NFR-S3 (Session Integrity)**: Admin session cookies must be signed with `HMAC-SHA256`, marked `HttpOnly`, set with `SameSite=Lax`, and protected against tampering.
- **NFR-S4 (Input Sanitization & Injection Defense)**: All incoming payloads must be strictly typed and validated via Pydantic v2 schemas; ORM queries must use parameterized statements to eliminate SQL injection vulnerabilities.
- **NFR-S5 (Prompt Injection Mitigation)**: User feedback prompts must be strictly encapsulated in structured prompt templates to prevent prompt injection hijacking.

---

### 3. Reliability & Fault Tolerance
- **NFR-R1 (Zero-Downtime AI Graceful Degradation)**: If the Google Gemini API fails (rate limiting 429, invalid key 401/403, or network timeout), the application must automatically switch to the deterministic fallback engine without throwing 500 error pages.
- **NFR-R2 (Database Consistency)**: Database transactions must adhere strictly to ACID properties with foreign key constraints enabled.
- **NFR-R3 (Graceful Error Handling)**: Universal exception handlers must catch 404, 422, and 500 exceptions, returning stylized user-friendly error views while masking internal stack traces in production mode.

---

### 4. Usability & User Experience (UX)
- **NFR-U1 (Design System)**: The interface must adhere to a premium athletic dark-mode aesthetic utilizing deep charcoal backgrounds (`#0B0E14`), high-contrast card surfaces (`#161B26`), electric neon accents (Volt Lime `#C8FF00`, Cyan `#00F0FF`), and modern typography (Outfit / Inter).
- **NFR-U2 (Device Responsiveness)**: The web UI must be fully responsive across mobile phones (360px+), tablets (768px+), and desktop monitors (1200px+).
- **NFR-U3 (Clarity & Readability)**: Exercise instructions, sets, reps, and rest timers must be presented in scannable tabbed cards.

---

### 5. Maintainability & Code Quality
- **NFR-M1 (Modular Architecture)**: Codebase must maintain a strict layered structure separating Core, Database, Schemas, Routers, Services, Prompts, and Templates.
- **NFR-M2 (Automated Test Coverage)**: The project must maintain a comprehensive test suite covering all critical workflows with 100% passing tests.
- **NFR-M3 (Database Migration Traceability)**: All database schema modifications must be versioned and reversible via Alembic migration scripts.
