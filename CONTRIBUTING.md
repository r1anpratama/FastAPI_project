# Contributing to FastAPI Template

## Development Flow
- Utilize Docker Compose for database orchestration (docker-compose up -d).
- Run database migrations via Alembic (lembic upgrade head).
- Ensure all asynchronous database queries use async sessions.