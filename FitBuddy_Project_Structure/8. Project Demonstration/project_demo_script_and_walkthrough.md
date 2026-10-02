# Phase 8: Project Demonstration - Live Demo Script & Walkthrough

## 1. Demonstration Scenario & Objectives

This demonstration script provides a structured, 5-minute walkthrough showcasing the end-to-end capabilities of FitBuddy to stakeholders, evaluators, and end users.

---

## 2. Timed Presentation Walkthrough

### 🕒 Minute 0:00 - 0:45 | Introduction & Problem Overview
- **Visual**: FitBuddy Landing Page (`http://127.0.0.1:8000`).
- **Narrative**:
  - *"Welcome to FitBuddy. Traditional workout apps are static, expensive, and fail to adapt when life happens. FitBuddy is an AI-powered fitness application built with FastAPI, SQLAlchemy, and Google Gemini that creates customized 7-day workout plans and adapts dynamically to user feedback."*
- **Action**: Highlight the dark-mode athletic design and click **"Get Started"**.

---

### 🕒 Minute 0:45 - 1:45 | User Onboarding & AI Microcycle Generation
- **Visual**: Profile Questionnaire (`/profile`) transitioning to Generation Screen (`/generating`).
- **Narrative**:
  - *"We'll create a profile for Sarah, a 28-year-old beginner aiming for Weight Loss with Medium Intensity. When we submit, FitBuddy dispatches our request to the Google GenAI `gemini-2.5-flash` model using structured JSON schema enforcement."*
- **Action**: Fill out form and submit. Show the dynamic loader, followed by the instant render of the interactive 7-Day Workout Dashboard.

---

### 🕒 Minute 1:45 - 2:45 | Interactive 7-Day Microcycle Exploration
- **Visual**: 7-Day Workout Dashboard (`/workouts/{id}`).
- **Narrative**:
  - *"Notice the structure of each day: dynamic warmups, specific exercise sets, reps, rest intervals, safety cues, cool-downs, and recovery rules."*
- **Action**: Click across **Day 1**, **Day 2**, and **Day 3** tabs. Highlight the smooth tab switching and clear exercise cards.

---

### 🕒 Minute 2:45 - 3:45 | Adaptive Feedback & Plan Refinement Loop
- **Visual**: Feedback Modal (`/workouts/{id}/feedback`).
- **Narrative**:
  - *"Here is FitBuddy's standout feature: conversational plan remodeling. If Sarah wants to emphasize core work and lighten Day 3, she simply types it in plain English."*
- **Action**: Type: *"Please make Day 3 focused on core and low-impact cardio."* Click **"Submit Revision"**.
- **Outcome**: Show version upgrade from `v1.0` to `v2.0` with Day 3 updated accordingly.

---

### 🕒 Minute 3:45 - 4:30 | Goal-Driven Nutrition & Recovery Center
- **Visual**: Nutrition Guide (`/nutrition`).
- **Narrative**:
  - *"Training is only half the equation. FitBuddy generates tailored nutrition and recovery recommendations matched to Sarah's Weight Loss goal: protein pacing, meal timing, and sleep hygiene."*
- **Action**: Scroll through the nutrition cards.

---

### 🕒 Minute 4:30 - 5:00 | Admin Control Center & Telemetry
- **Visual**: Admin Login (`/admin/login`) & Dashboard (`/admin/dashboard`).
- **Narrative**:
  - *"Finally, administrators have access to a secure management portal featuring real-time KPI metrics, demographic distributions, and cascading user audits."*
- **Action**: Log in with `admin` / `adminpassword123`, inspect dashboard charts, and show clean system health.
