# Phase 5: Project Development Phase - Frontend & Templating Implementation

## 1. Template Hierarchy & Layout Inheritance

FitBuddy employs **Jinja2** template inheritance for maximum performance and consistent layout branding.

```text
app/templates/
├── base.html                   # Global HTML5 boilerplate, navigation bar, footer & disclaimers
├── index.html                  # High-conversion hero landing page
├── profile.html                # Multi-step user onboarding & questionnaire form
├── profile_view.html           # Profile inspection & saved routine manager
├── generating.html             # AI generation progress transition view
├── result.html                 # 7-Day interactive workout plan microcycle schedule
├── feedback.html               # Plan refinement modal & feedback revision view
├── nutrition.html              # Goal-driven nutrition & recovery center
├── history.html                # Plan version archive & audit logs
├── error.html                  # Universal error view (404, 422, 500)
└── admin/                      # Protected administrative templates
    ├── login.html              # Secure administrator authentication form
    ├── dashboard.html          # Real-time system KPI telemetry & user list
    └── user_detail.html        # Detailed user profile & plan audit
```

---

## 2. Athletic Dark-Mode CSS Architecture (`static/css/style.css`)

The application avoids generic design styles by utilizing a custom athletic design system:

```css
:root {
  --bg-primary: #0b0e14;
  --bg-surface: #161b26;
  --bg-card: #1f2633;
  --accent-volt: #c8ff00;
  --accent-cyan: #00f0ff;
  --text-primary: #f8fafc;
  --text-secondary: #94a3b8;
  --border-subtle: #2d3748;
  --radius-lg: 16px;
  --radius-md: 10px;
  --shadow-glow: 0 0 20px rgba(200, 255, 0, 0.25);
}
```

---

## 3. Dynamic Microcycle Tab Controller (`static/js/app.js`)

Interactive day switching is implemented using lightweight Vanilla JavaScript:

- **Tab Switching**: Toggles the active day card and animates exercise routines instantly without page reloads.
- **Feedback Trigger**: Opens and closes the plan revision modal with smooth backdrop blur transitions.
- **Loading State**: Disables buttons, updates text to *"AI Generating..."*, and activates CSS glow spinners during API dispatches.
