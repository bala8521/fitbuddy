# Phase 4: Project Planning Phase - Risk Management & Mitigation Matrix

## 1. Risk Assessment Framework

Risks are categorized based on **Likelihood** (Low / Medium / High) and **Impact** (Low / Medium / High), with corresponding mitigation and contingency plans.

---

## 2. Risk Matrix Table

| Risk ID | Identified Risk Event | Likelihood | Impact | Severity | Mitigation Strategy | Contingency Plan |
|---|---|---|---|---|---|---|
| **RSK-01** | **Gemini API Rate Limiting or Outage** | Medium | High | **High** | Implement request timeout guards and graceful error catching. | Automatic failover to built-in deterministic workout generator with zero user interruption. |
| **RSK-02** | **AI Hallucination / Malformed JSON** | Medium | High | **High** | Enforce strict Pydantic v2 validation models and JSON schemas on AI output responses. | Schema validation retry logic with fallback recovery if parsing fails. |
| **RSK-03** | **Prompt Injection via Feedback Input** | Low | Medium | **Medium** | Treat all user inputs as data parameters within structured templates; apply input length boundaries (500 chars). | Reject malformed or excessively long inputs before reaching AI layer. |
| **RSK-04** | **Database Concurrency & Locking (SQLite)** | Low | Medium | **Medium** | Enable WAL (Write-Ahead Logging) mode and connection timeouts; maintain stateless connection pooling. | Ready-to-use PostgreSQL migration config for high-concurrency production deployments. |
| **RSK-05** | **Session Cookie Hijacking / Tampering** | Low | High | **High** | Sign session cookies using `HMAC-SHA256` with strong secret keys; apply `HttpOnly` and `SameSite=Lax` flags. | Invalidate tampered cookies and force administrator re-authentication. |
| **RSK-06** | **Health / Medical Liability Claims** | Low | High | **High** | Prominently display explicit health & medical disclaimers in UI navigation footer and onboarding forms. | Require acknowledgment that FitBuddy provides general educational routines, not clinical advice. |
