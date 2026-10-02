# Phase 3: Project Design Phase - REST API Design Specification

## 1. Overview & Conventions

FitBuddy exposes a RESTful API with JSON payload contracts. All request bodies and response schemas are strictly enforced using Pydantic v2 validation models.

- **Base URL**: `/api`
- **Content-Type**: `application/json`
- **Status Codes**: Standard HTTP status codes (`200 OK`, `201 Created`, `400 Bad Request`, `404 Not Found`, `422 Validation Error`, `500 Server Error`).

---

## 2. API Endpoints Table

| Method | Endpoint | Description | Request Body | Response Status |
|---|---|---|---|---|
| `GET` | `/health` | Root system health check | None | `200 OK` |
| `GET` | `/api/health` | Comprehensive DB & Gemini health | None | `200 OK` |
| `POST` | `/api/users` | Create new user profile | `UserCreate` JSON | `201 Created` |
| `GET` | `/api/users/{user_id}` | Get user profile by ID | None | `200 OK` |
| `GET` | `/api/users` | List paginated users (`skip`, `limit`) | Query Params | `200 OK` |
| `POST` | `/api/workouts/generate` | Generate 7-day AI workout plan | `{"user_id": int}` | `201 Created` |
| `GET` | `/api/workouts/{plan_id}` | Retrieve specific workout plan | None | `200 OK` |
| `GET` | `/api/workouts/user/{user_id}` | Retrieve all workout plans for user | None | `200 OK` |
| `POST` | `/api/workouts/{plan_id}/feedback` | Submit refinement feedback | `FeedbackCreate` JSON | `200 OK` |
| `GET` | `/api/workouts/{plan_id}/feedback` | Get revision history for plan | None | `200 OK` |
| `POST` | `/api/nutrition/tip` | Generate goal-aligned nutrition tip | `NutritionRequest` JSON | `201 Created` |
| `GET` | `/api/nutrition/tips` | List recent nutrition tips | Query Params | `200 OK` |
| `GET` | `/api/admin/metrics` | System analytics & KPI telemetry | None (Session Cookie) | `200 OK` |

---

## 3. Sample Payloads & Contracts

### 1. User Creation (`POST /api/users`)
**Request:**
```json
{
  "name": "Sarah Jenkins",
  "age": 28,
  "gender": "Female",
  "weight": 64.5,
  "goal": "Weight Loss",
  "intensity": "Medium",
  "experience": "Beginner"
}
```

**Response (`201 Created`):**
```json
{
  "id": 1,
  "name": "Sarah Jenkins",
  "age": 28,
  "gender": "Female",
  "weight": 64.5,
  "goal": "Weight Loss",
  "intensity": "Medium",
  "experience": "Beginner",
  "created_at": "2026-10-02T08:00:00Z"
}
```

---

### 2. Workout Generation (`POST /api/workouts/generate`)
**Request:**
```json
{
  "user_id": 1
}
```

**Response (`201 Created`):**
```json
{
  "id": 101,
  "user_id": 1,
  "title": "7-Day Personalized Weight Loss Microcycle",
  "goal": "Weight Loss",
  "intensity": "Medium",
  "version": "1.0",
  "is_active": true,
  "days": [
    {
      "day_number": 1,
      "day_name": "Monday",
      "focus": "Full Body Metabolic Conditioning",
      "warmup": "5 min dynamic leg swings, arm circles, and light jumping jacks",
      "cooldown": "5 min static hamstring, quad, and shoulder stretching",
      "recovery": "Hydrate with 2.5L water, target 8 hours of sleep",
      "exercises": [
        {
          "order_index": 1,
          "name": "Bodyweight Squats",
          "target_muscle": "Quadriceps & Glutes",
          "sets": 3,
          "reps": "12-15 reps",
          "rest_seconds": 60,
          "form_cues": "Keep chest high, knees tracking over toes, engage core."
        }
      ]
    }
  ]
}
```

---

### 3. Feedback Revision (`POST /api/workouts/101/feedback`)
**Request:**
```json
{
  "feedback_text": "Please make Day 3 a dedicated core and low-impact cardio session."
}
```

**Response (`200 OK`):**
```json
{
  "message": "Workout plan refined successfully based on your feedback.",
  "previous_version": "1.0",
  "new_version": "2.0",
  "plan": {
    "id": 101,
    "version": "2.0",
    "title": "7-Day Personalized Weight Loss Microcycle (Refined)"
  }
}
```
