# Phase 5: Project Development Phase - AI Prompt Engineering & Gemini GenAI Integration

## 1. Google GenAI SDK Client Setup

FitBuddy leverages Google's official `google-genai` Python SDK targeting the high-speed, cost-efficient `gemini-2.5-flash` model.

```python
from google import genai
from google.genai import types

client = genai.Client(api_key=settings.GEMINI_API_KEY)
```

---

## 2. Prompt Engineering Architecture

### 1. System Instruction Definition
The AI model is configured with an authoritative system persona:
> *"You are an elite, certified strength and conditioning specialist (CSCS) and sports nutritionist. You create safe, structured, periodized 7-day fitness plans tailored precisely to an individual's biometric profile, goals, and training intensity. Always return your responses strictly in valid JSON matching the exact schema provided."*

### 2. Structured JSON Schema Enforcement
FitBuddy instructs Gemini to format responses according to strict JSON schemas:

```json
{
  "title": "7-Day Personalized Muscle Gain Microcycle",
  "goal": "Muscle Gain",
  "intensity": "High",
  "days": [
    {
      "day_number": 1,
      "day_name": "Monday",
      "focus": "Upper Body Push (Chest, Shoulders, Triceps)",
      "warmup": "5 min arm circles, band pull-aparts, light push-ups",
      "cooldown": "5 min chest & triceps static stretching",
      "recovery": "Target 160g protein, hydrate with 3L water",
      "exercises": [
        {
          "order_index": 1,
          "name": "Barbell Bench Press",
          "target_muscle": "Pectoralis Major",
          "sets": 4,
          "reps": "8-10 reps",
          "rest_seconds": 90,
          "form_cues": "Retract scapulae, touch lower chest, drive feet into floor."
        }
      ]
    }
  ]
}
```

---

## 3. High-Resilience Deterministic Fallback Engine

When the Gemini API is offline, experiencing rate-limiting (`429`), or when `GEMINI_API_KEY` is not provided, FitBuddy executes `_generate_deterministic_fallback()`:

1. Evaluates user's `goal` (*Weight Loss*, *Muscle Gain*, *General Wellness*).
2. Evaluates user's `intensity` (*Low*, *Medium*, *High*) and `experience` level.
3. Constructs a 7-day routine based on certified exercise science templates:
   - **Muscle Gain**: Push / Pull / Legs / Rest / Upper / Lower / Active Recovery
   - **Weight Loss**: Full Body HIIT / Cardio / Core / Active Recovery / Circuit Training
   - **General Wellness**: Mobility / Moderate Resistance / Aerobic Endurance / Yoga Recovery
4. Calculates progressive set/rep schemes dynamically.
5. Delivers the plan with zero downtime and logs an informational telemetry warning.
