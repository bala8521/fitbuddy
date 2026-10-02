# Phase 2: Requirement Analysis - Functional Requirements

## 1. Overview

This document specifies the complete functional requirements (FRs) for the FitBuddy application. Every requirement is assigned a unique identifier, priority level, and detailed behavioral criteria.

---

## 2. Detailed Functional Requirements

### Module 1: User Profile Management

| Req ID | Title | Description | Priority |
|---|---|---|---|
| **FR-01.1** | Profile Creation | The system shall capture user profile attributes including Name, Age (14–100), Gender, Weight (30–300 kg), Primary Goal, Workout Intensity, and Experience Level. | **High** |
| **FR-01.2** | Input Validation | The system shall enforce boundary and type checks on all user input fields using Pydantic v2 schemas and return clear validation errors on failure. | **High** |
| **FR-01.3** | Profile Persistence | The system shall persist user records in the relational database with auto-generated primary keys and creation timestamps. | **High** |
| **FR-01.4** | Profile Retrieval | The system shall provide endpoints to retrieve individual profile details as well as paginated lists of profiles. | **Medium** |

---

### Module 2: 7-Day AI Workout Plan Generation

| Req ID | Title | Description | Priority |
|---|---|---|---|
| **FR-02.1** | Microcycle Generation | The system shall generate a comprehensive 7-day workout plan based on the user's age, goal, intensity, and experience. | **High** |
| **FR-02.2** | Daily Session Structure | Each day within the plan must contain: Day Name, Daily Focus/Theme, Warmup Drills (5-8 min), 3 to 5 Primary Exercises, Cool-down Stretches (5 min), and Recovery/Rest notes. | **High** |
| **FR-02.3** | Exercise Schema | Each exercise item must specify Exercise Name, Target Muscle Group, Number of Sets, Reps/Duration, Rest Period (in seconds), and Form/Safety Cues. | **High** |
| **FR-02.4** | AI Orchestration | The system shall send structured system prompts and user profile contexts to the Google GenAI (`gemini-2.5-flash`) API with JSON schema enforcement. | **High** |
| **FR-02.5** | Offline Fallback Support | In case of missing API keys, network errors, timeouts, or quota limits, the system shall seamlessly fall back to an internal expert-verified workout generation engine. | **High** |

---

### Module 3: Plan Refinement & Feedback Loop

| Req ID | Title | Description | Priority |
|---|---|---|---|
| **FR-03.1** | Feedback Submission | The system shall allow users to submit natural language modification requests (e.g., *"More focus on cardio"*, *"Make Friday a rest day"*). | **High** |
| **FR-03.2** | Plan Remodeling | The AI engine shall analyze the existing plan alongside the feedback and generate a revised 7-day microcycle adhering to the requested changes. | **High** |
| **FR-03.3** | Plan Version Tracking | The system shall increment the plan's version identifier (e.g., `v1.0` -> `v2.0`) and record feedback history without destroying original base plans. | **High** |
| **FR-03.4** | Historical Archive | The system shall allow users to view previous workout plan versions and past feedback logs. | **Medium** |

---

### Module 4: Nutrition & Recovery Guidance

| Req ID | Title | Description | Priority |
|---|---|---|---|
| **FR-04.1** | Goal-Tailored Advice | The system shall provide actionable dietary recommendations matched to the user's primary goal (*Weight Loss*, *Muscle Gain*, *General Wellness*). | **High** |
| **FR-04.2** | Macronutrient & Hydration Rules | The system shall supply protein distribution guidelines, pre/post workout meal ideas, and daily water intake targets. | **Medium** |
| **FR-04.3** | Sleep Hygiene Protocols | The system shall include sleep optimization strategies (e.g., 7–9 hours, circadian alignment, blue light reduction) to maximize athletic recovery. | **Medium** |

---

### Module 5: Administrative Control & Monitoring

| Req ID | Title | Description | Priority |
|---|---|---|---|
| **FR-05.1** | Secure Admin Login | The system shall authenticate administrators using PBKDF2-HMAC-SHA256 password hashing and cryptographically signed session cookies. | **High** |
| **FR-05.2** | System KPI Dashboard | The admin portal shall display aggregate real-time metrics: Total Users, Total Plans Generated, Feedback Submissions, Goal Distributions, and Average Age. | **High** |
| **FR-05.3** | User Profile Audit | The admin portal shall enable inspection of user profiles, generated plans, and revision histories. | **Medium** |
| **FR-05.4** | Account Deletion | The admin portal shall provide cascading deletion of user accounts and associated workout/feedback records. | **Medium** |
