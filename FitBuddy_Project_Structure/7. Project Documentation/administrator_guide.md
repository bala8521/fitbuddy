# Phase 7: Project Documentation - Administrator Operations Guide

## 1. Administrative Overview & Access Control

FitBuddy provides a secure administrative control center designed for system telemetry, performance monitoring, user management, and data audits.

- **Admin Login URL**: `http://127.0.0.1:8000/admin/login`
- **Default Credentials** (Configured via `.env`):
  - **Username**: `admin`
  - **Password**: `adminpassword123`

---

## 2. Administrator Dashboard Features

### 1. Real-Time KPI Telemetry Cards
- **Total Registered Users**: Total count of active user profiles.
- **Total Plans Generated**: Sum of initial plans and AI remodeled plans.
- **Feedback Revisions**: Total feedback refinement requests submitted.
- **Average User Age**: Mean demographic age across all registered users.

### 2. Goal Distribution Analytics
Displays proportional breakdowns of fitness goals across all platform users:
- 🔵 **Weight Loss**: % of user base
- 🟢 **Muscle Gain**: % of user base
- 🟣 **General Wellness**: % of user base

### 3. User Audit & Management Table
- Search and list registered users with pagination.
- Inspect user profile details, active plan versions, and feedback histories.
- **Cascading Account Deletion**: Safely delete user records, automatically purging associated workout plans, daily routines, exercises, feedback logs, and nutrition tips.

---

## 3. Administrator Security Best Practices

1. **Change Default Password**: Immediately update `ADMIN_PASSWORD` in your `.env` file before deploying to production.
2. **Rotate Secret Keys**: Ensure `SECRET_KEY` is a minimum 32-character random string to prevent cookie forgery.
3. **Session Timeout**: Admin sessions automatically expire after 24 hours.
