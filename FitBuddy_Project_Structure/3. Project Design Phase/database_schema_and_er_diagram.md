# Phase 3: Project Design Phase - Database Schema & ER Diagram

## 1. Database Overview

FitBuddy uses a fully normalized relational schema designed with SQLAlchemy 2.0 ORM. The schema ensures data integrity, enforces foreign key relationships, supports cascading deletes, and provides efficient query indexing.

---

## 2. Entity-Relationship (ER) Diagram

```mermaid
erDiagram
    USERS ||--o{ WORKOUT_PLANS : "creates"
    USERS ||--o{ NUTRITION_TIPS : "receives"
    WORKOUT_PLANS ||--|{ DAILY_WORKOUTS : "contains (7 days)"
    DAILY_WORKOUTS ||--|{ EXERCISES : "includes"
    WORKOUT_PLANS ||--o{ FEEDBACK_HISTORY : "tracks"

    USERS {
        int id PK "Primary Key"
        string name "User Full Name"
        int age "Age (14-100)"
        string gender "Gender"
        float weight "Weight in KG"
        string goal "Weight Loss / Muscle Gain / General Wellness"
        string intensity "Low / Medium / High"
        string experience "Beginner / Intermediate / Advanced"
        datetime created_at "Creation Timestamp"
        datetime updated_at "Update Timestamp"
    }

    WORKOUT_PLANS {
        int id PK "Primary Key"
        int user_id FK "Foreign Key to USERS.id (CASCADE)"
        string title "Plan Title"
        string goal "Target Goal"
        string intensity "Workout Intensity"
        string version "Version string (e.g., v1.0, v2.0)"
        boolean is_active "Active Status"
        datetime created_at "Creation Timestamp"
    }

    DAILY_WORKOUTS {
        int id PK "Primary Key"
        int plan_id FK "Foreign Key to WORKOUT_PLANS.id (CASCADE)"
        int day_number "Day Index (1 to 7)"
        string day_name "Day Name (e.g., Monday)"
        string focus "Daily Focus / Target"
        string warmup "Dynamic Warmup Drills"
        string cooldown "Cool-down Stretches"
        string recovery "Recovery / Rest Protocols"
    }

    EXERCISES {
        int id PK "Primary Key"
        int daily_workout_id FK "Foreign Key to DAILY_WORKOUTS.id (CASCADE)"
        int order_index "Execution Sequence"
        string name "Exercise Name"
        string target_muscle "Target Muscle Group"
        int sets "Number of Sets"
        string reps "Repetitions or Duration"
        int rest_seconds "Rest Duration in Seconds"
        string form_cues "Form & Safety Guidance"
    }

    FEEDBACK_HISTORY {
        int id PK "Primary Key"
        int plan_id FK "Foreign Key to WORKOUT_PLANS.id (CASCADE)"
        string feedback_text "Natural Language User Request"
        string previous_version "Previous Version (e.g., v1.0)"
        string new_version "New Version (e.g., v2.0)"
        datetime created_at "Submission Timestamp"
    }

    NUTRITION_TIPS {
        int id PK "Primary Key"
        int user_id FK "Foreign Key to USERS.id (CASCADE)"
        string goal "Associated Goal"
        string tip_title "Guidance Title"
        text tip_content "Structured Nutrition Guidelines"
        datetime created_at "Creation Timestamp"
    }
```

---

## 3. Detailed Table Specifications

### Table 1: `users`
- `id` (INTEGER, Primary Key, Autoincrement)
- `name` (VARCHAR(100), NOT NULL)
- `age` (INTEGER, NOT NULL)
- `gender` (VARCHAR(20), NOT NULL)
- `weight` (FLOAT, NOT NULL)
- `goal` (VARCHAR(50), NOT NULL)
- `intensity` (VARCHAR(20), NOT NULL)
- `experience` (VARCHAR(20), NOT NULL)
- `created_at` (DATETIME, Default: UTC Now)
- `updated_at` (DATETIME, Default: UTC Now, onupdate: UTC Now)

### Table 2: `workout_plans`
- `id` (INTEGER, Primary Key, Autoincrement)
- `user_id` (INTEGER, Foreign Key `users.id` ON DELETE CASCADE, Index)
- `title` (VARCHAR(150), NOT NULL)
- `goal` (VARCHAR(50), NOT NULL)
- `intensity` (VARCHAR(20), NOT NULL)
- `version` (VARCHAR(10), Default: `"1.0"`)
- `is_active` (BOOLEAN, Default: `True`)
- `created_at` (DATETIME, Default: UTC Now)

### Table 3: `daily_workouts`
- `id` (INTEGER, Primary Key, Autoincrement)
- `plan_id` (INTEGER, Foreign Key `workout_plans.id` ON DELETE CASCADE, Index)
- `day_number` (INTEGER, NOT NULL)
- `day_name` (VARCHAR(20), NOT NULL)
- `focus` (VARCHAR(100), NOT NULL)
- `warmup` (TEXT, NOT NULL)
- `cooldown` (TEXT, NOT NULL)
- `recovery` (TEXT, NULLABLE)

### Table 4: `exercises`
- `id` (INTEGER, Primary Key, Autoincrement)
- `daily_workout_id` (INTEGER, Foreign Key `daily_workouts.id` ON DELETE CASCADE, Index)
- `order_index` (INTEGER, NOT NULL)
- `name` (VARCHAR(100), NOT NULL)
- `target_muscle` (VARCHAR(50), NOT NULL)
- `sets` (INTEGER, NOT NULL)
- `reps` (VARCHAR(30), NOT NULL)
- `rest_seconds` (INTEGER, Default: 60)
- `form_cues` (TEXT, NULLABLE)

### Table 5: `feedback_history`
- `id` (INTEGER, Primary Key, Autoincrement)
- `plan_id` (INTEGER, Foreign Key `workout_plans.id` ON DELETE CASCADE, Index)
- `feedback_text` (TEXT, NOT NULL)
- `previous_version` (VARCHAR(10), NOT NULL)
- `new_version` (VARCHAR(10), NOT NULL)
- `created_at` (DATETIME, Default: UTC Now)

### Table 6: `nutrition_tips`
- `id` (INTEGER, Primary Key, Autoincrement)
- `user_id` (INTEGER, Foreign Key `users.id` ON DELETE CASCADE, Index)
- `goal` (VARCHAR(50), NOT NULL)
- `tip_title` (VARCHAR(150), NOT NULL)
- `tip_content` (TEXT, NOT NULL)
- `created_at` (DATETIME, Default: UTC Now)
