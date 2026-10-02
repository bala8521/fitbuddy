# Phase 2: Requirement Analysis - Use Case Specifications

## 1. Actors

1. **Fitness User (Primary)**: An individual creating a profile, generating workouts, refining plans, and consuming nutrition advice.
2. **System Administrator (Secondary)**: Authorized manager accessing analytics, auditing user accounts, and managing system data.
3. **Google GenAI Engine (External)**: Large language model API providing dynamic workout routine construction.

---

## 2. Key Use Case Specifications

### Use Case UC-01: Create User Profile & Generate 7-Day Workout Plan
- **Primary Actor**: Fitness User
- **Preconditions**: User navigates to the FitBuddy application.
- **Main Flow**:
  1. User clicks "Get Started" or "Create Profile".
  2. System renders the Profile Onboarding questionnaire.
  3. User enters Name, Age, Gender, Weight, Goal (*Weight Loss*, *Muscle Gain*, *General Wellness*), Workout Intensity, and Experience Level.
  4. User submits the form.
  5. System validates inputs against Pydantic schema `UserCreate`.
  6. System creates a `User` database record.
  7. System invokes `WorkoutService.generate_plan()`, dispatching prompts to Google Gemini API (`gemini-2.5-flash`).
  8. Gemini API returns structured 7-day JSON plan.
  9. System persists the `WorkoutPlan` and associated `DailyWorkout` and `Exercise` records.
  10. System displays the interactive 7-Day Workout Microcycle interface with day selector tabs.
- **Alternative Flow (AI Service Unavailable)**:
  - At step 8, if Gemini API fails or key is missing, system invokes `fallback_engine.generate()`, logs a warning, and delivers the plan seamlessly.
- **Postconditions**: User profile and initial `v1.0` workout plan are stored in database and displayed on screen.

---

### Use Case UC-02: Submit Plan Refinement Feedback
- **Primary Actor**: Fitness User
- **Preconditions**: User has an existing active workout plan.
- **Main Flow**:
  1. User navigates to the active plan view and clicks "Refine Plan" / "Give Feedback".
  2. System displays the feedback submission modal.
  3. User types specific modification requests (*e.g., "Add 15 minutes of cardio on Day 2 and make Day 4 upper body focused"*).
  4. User clicks "Submit Revision".
  5. System loads current plan and user profile, constructing a revision prompt for Gemini AI.
  6. Gemini AI remodels the 7-day microcycle preserving valid exercises while incorporating user modifications.
  7. System saves the new plan version (`v2.0`), records entry in `FeedbackHistory`, and updates the active plan view.
  8. User is presented with the updated plan and a confirmation toast.
- **Postconditions**: Plan version is incremented, feedback record is linked, and updated schedule is displayed.

---

### Use Case UC-03: View Nutrition & Recovery Center
- **Primary Actor**: Fitness User
- **Preconditions**: User has selected a fitness goal.
- **Main Flow**:
  1. User selects "Nutrition & Recovery" from top navigation or plan dashboard.
  2. System queries `NutritionService` with user's primary goal.
  3. System renders goal-aligned dietary guidelines, protein pacing rules, hydration benchmarks, and recovery/sleep protocols.
- **Postconditions**: Nutrition recommendations are displayed on screen.

---

### Use Case UC-04: Admin Authentication & Metric Inspection
- **Primary Actor**: System Administrator
- **Preconditions**: Admin navigates to `/admin/login`.
- **Main Flow**:
  1. Admin inputs username and password.
  2. System queries `AdminService`, validating PBKDF2-HMAC-SHA256 password hash.
  3. System sets an HMAC-SHA256 signed session cookie and redirects to `/admin/dashboard`.
  4. System computes real-time KPI metrics:
     - Total registered users
     - Total workout plans generated
     - Plan modification feedback count
     - Goal distribution charts (Weight Loss vs Muscle Gain vs General Wellness)
     - Average user age and intensity distribution
  5. System renders interactive dashboard and user management table.
- **Postconditions**: Admin gains authorized access to system health and user audit records.
