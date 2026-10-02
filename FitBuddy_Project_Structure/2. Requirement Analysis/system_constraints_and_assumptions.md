# Phase 2: Requirement Analysis - System Constraints & Assumptions

## 1. System Assumptions

1. **User Connectivity**: Users possess modern HTML5/CSS3-compatible web browsers (Chrome, Firefox, Safari, Edge) on desktop or mobile devices with stable internet access.
2. **AI Model Availability**: Google GenAI's `gemini-2.5-flash` model endpoint is accessible via standard HTTPS over port 443 with a valid API key.
3. **User Health Assumption**: Users are assumed to be in reasonable general physical condition and cleared by medical practitioners for physical activity before following AI recommendations.

---

## 2. Technical & Hardware Constraints

### 1. Technology Constraints
- **Language & Runtime**: Python 3.11 or higher.
- **Web Framework**: FastAPI ASGI framework with Uvicorn.
- **Database Support**: SQLite 3 with Foreign Keys pragma enabled for local development; PostgreSQL 14+ for production environments.
- **Client Requirements**: No heavy JavaScript framework required; Vanilla ES6+ and Vanilla CSS used to maintain lightweight execution and fast load times.

### 2. Operational Constraints
- **API Token Limits**: Gemini API calls are managed with concise system prompts and strict JSON structured schemas to prevent excessive token consumption and stay within free/standard tier quotas.
- **Stateless Web Layer**: The FastAPI application remains stateless, allowing horizontal scaling behind load balancers with session state persisted in signed cookies and relational databases.

---

## 3. Legal, Compliance & Health Disclaimers

> [!CAUTION]
> **Health & Safety Medical Disclaimer**:
> FitBuddy is an artificial intelligence-powered fitness planning and educational platform. It provides generalized training routines and dietary guidance based on user inputs. **FitBuddy is NOT a healthcare provider, medical clinic, or certified dietitian, and does NOT provide medical diagnosis, prescription, or clinical rehabilitation advice.** Users must consult with a licensed physician or healthcare professional before beginning any physical exercise regimen. If dizziness, pain, or shortness of breath occurs, exercise must be stopped immediately.
