# Phase 6: Project Testing - Test Cases & Traceability Matrix

## 1. Test Traceability Matrix

The FitBuddy test suite contains **31 automated test cases** mapped directly to system requirements:

| Test File | Test Case ID | Description | Target Requirement | Status |
|---|---|---|---|---|
| `test_health.py` | `TC-HLTH-01` | Test root `/health` returns 200 OK & healthy status | FR-01, NFR-P1 | **PASS** |
| `test_health.py` | `TC-HLTH-02` | Test `/api/health` reports DB & Gemini status | FR-01, NFR-R1 | **PASS** |
| `test_health.py` | `TC-HLTH-03` | Test landing page `/` renders HTML successfully | FR-01, NFR-U1 | **PASS** |
| `test_users.py` | `TC-USER-01` | Test valid user profile creation via `POST /api/users` | FR-01.1, FR-01.3 | **PASS** |
| `test_users.py` | `TC-USER-02` | Test profile creation rejects invalid age (< 14 or > 100) | FR-01.2 | **PASS** |
| `test_users.py` | `TC-USER-03` | Test profile creation rejects invalid weight (< 30kg) | FR-01.2 | **PASS** |
| `test_users.py` | `TC-USER-04` | Test profile creation rejects unsupported fitness goal | FR-01.2 | **PASS** |
| `test_users.py` | `TC-USER-05` | Test retrieve user profile by ID (`GET /api/users/{id}`) | FR-01.4 | **PASS** |
| `test_users.py` | `TC-USER-06` | Test retrieve non-existent user returns 404 Not Found | FR-01.4, NFR-R3 | **PASS** |
| `test_users.py` | `TC-USER-07` | Test paginated user listing (`GET /api/users`) | FR-01.4 | **PASS** |
| `test_workouts.py` | `TC-WORK-01` | Test 7-day plan generation for Weight Loss goal | FR-02.1, FR-02.2 | **PASS** |
| `test_workouts.py` | `TC-WORK-02` | Test 7-day plan generation for Muscle Gain goal | FR-02.1, FR-02.2 | **PASS** |
| `test_workouts.py` | `TC-WORK-03` | Test 7-day plan contains exactly 7 daily workouts | FR-02.2 | **PASS** |
| `test_workouts.py` | `TC-WORK-04` | Test daily workout includes Warmup, Cooldown, Exercises | FR-02.2, FR-02.3 | **PASS** |
| `test_workouts.py` | `TC-WORK-05` | Test exercise schema attributes (sets, reps, rest, cues) | FR-02.3 | **PASS** |
| `test_workouts.py` | `TC-WORK-06` | Test deterministic fallback generation on AI failure | FR-02.5, NFR-R1 | **PASS** |
| `test_workouts.py` | `TC-WORK-07` | Test retrieve workout plan by ID (`GET /api/workouts/{id}`) | FR-02.1 | **PASS** |
| `test_workouts.py` | `TC-WORK-08` | Test retrieve all plans for a user (`GET /api/workouts/user/{id}`) | FR-02.1 | **PASS** |
| `test_feedback.py` | `TC-FEED-01` | Test plan feedback refinement increments version (`v1.0 -> v2.0`) | FR-03.1, FR-03.3 | **PASS** |
| `test_feedback.py` | `TC-FEED-02` | Test feedback submission persists entry in `FeedbackHistory` | FR-03.1, FR-03.3 | **PASS** |
| `test_feedback.py` | `TC-FEED-03` | Test multiple feedback revisions increment sequentially (`v2.0 -> v3.0`) | FR-03.3 | **PASS** |
| `test_feedback.py` | `TC-FEED-04` | Test feedback on non-existent plan returns 404 | FR-03.1, NFR-R3 | **PASS** |
| `test_nutrition.py` | `TC-NUTR-01` | Test generate nutrition tip for Weight Loss goal | FR-04.1 | **PASS** |
| `test_nutrition.py` | `TC-NUTR-02` | Test generate nutrition tip for Muscle Gain goal | FR-04.1 | **PASS** |
| `test_nutrition.py` | `TC-NUTR-03` | Test generate nutrition tip for General Wellness goal | FR-04.1 | **PASS** |
| `test_nutrition.py` | `TC-NUTR-04` | Test list recent nutrition tips (`GET /api/nutrition/tips`) | FR-04.1 | **PASS** |
| `test_admin.py` | `TC-ADMN-01` | Test valid admin login sets signed session cookie | FR-05.1, NFR-S3 | **PASS** |
| `test_admin.py` | `TC-ADMN-02` | Test invalid admin credentials rejected (401 Unauthorized) | FR-05.1 | **PASS** |
| `test_admin.py` | `TC-ADMN-03` | Test unauthenticated access to `/admin/dashboard` redirects to login | FR-05.1, NFR-S3 | **PASS** |
| `test_admin.py` | `TC-ADMN-04` | Test admin metrics calculation (`GET /api/admin/metrics`) | FR-05.2 | **PASS** |
| `test_admin.py` | `TC-ADMN-05` | Test admin cascading user deletion removes plans & feedback | FR-05.4, NFR-R2 | **PASS** |
