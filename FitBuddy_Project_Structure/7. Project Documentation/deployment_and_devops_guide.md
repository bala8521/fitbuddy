# Phase 7: Project Documentation - Deployment & DevOps Guide

## 1. Production Architecture Overview

For production deployments, FitBuddy is configured to run behind an ASGI application server (Gunicorn + Uvicorn workers) reverse-proxied by Nginx or Cloudflare with SSL/TLS termination and a PostgreSQL database.

```
+----------------+      HTTPS       +---------------+      Proxy Pass     +-------------------------+
|  Web Browsers  | --------------> |  Nginx / SSL  | ------------------> |  Gunicorn / Uvicorn     |
+----------------+                 +---------------+                     |  FastAPI (Workers: 4)   |
                                                                         +------------+------------+
                                                                                      |
                                                                                      v
                                                                         +-------------------------+
                                                                         |  PostgreSQL Database    |
                                                                         +-------------------------+
```

---

## 2. Docker Containerization Setup

### `Dockerfile`
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY . .

# Run database migrations and launch server
EXPOSE 8000
CMD ["sh", "-c", "python -m alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4"]
```

---

## 3. Production Environment Checklist

1. **Set `ENVIRONMENT=production`** and `DEBUG=False` in `.env`.
2. **Switch Database URL** from SQLite to managed PostgreSQL (`postgresql+psycopg2://user:pass@host:5432/fitbuddy_db`).
3. **Generate Secure `SECRET_KEY`** (e.g. using `python -c "import secrets; print(secrets.token_urlsafe(32))"`).
4. **Provision Valid `GEMINI_API_KEY`** from Google AI Studio.
5. **Configure SSL / HTTPS** via Let's Encrypt or Cloudflare.
