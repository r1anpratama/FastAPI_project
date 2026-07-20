<h1 align="center">
  FastAPI Web Scraper & API
</h1>

<p align="center">
  <a href="https://fastapi.tiangolo.com/"><img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI"></a>
  <a href="https://www.postgresql.org/"><img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL"></a>
  <a href="https://www.sqlalchemy.org/"><img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy"></a>
  <a href="https://www.docker.com/"><img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"></a>
  <a href="https://docs.python.org/3/library/asyncio.html"><img src="https://img.shields.io/badge/asyncio-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Asyncio"></a>
</p>

<p align="center">
  <strong>A production-grade REST API template built with FastAPI, asynchronous SQLAlchemy, and a built-in web scraper.</strong>
</p>

## 🚀 Features

- **⚡ High Performance:** Built on FastAPI, leveraging Starlette and Pydantic for maximum speed.
- **🗄️ Asynchronous Database:** Fully async database operations using SQLAlchemy 2.0 and `asyncpg` with PostgreSQL.
- **🔄 Database Migrations:** Integrated with Alembic for robust schema management.
- **🕷️ Built-in Scraper:** Includes a BeautifulSoup4 and httpx based scraper to fetch data efficiently.
- **🐳 Dockerized Environment:** Pre-configured `docker-compose.yml` for seamless development and deployment.
- **📁 Professional Structure:** Adheres to enterprise-grade repository structures and best practices.

## 📂 Project Structure

```text
├── app/
│   ├── api/          # API Routers and Dependencies
│   ├── core/         # Core configurations (Pydantic Settings)
│   ├── db/           # SQLAlchemy Engine, Session, and Models
│   ├── schemas/      # Pydantic Schemas for Validation
│   ├── services/     # Business logic and Scraper implementations
│   └── main.py       # FastAPI Application Entrypoint
├── alembic/          # Migration scripts and environment
├── Dockerfile        # Container build instructions
├── docker-compose.yml# Container orchestration
└── requirements.txt  # Python dependencies
```

## 🛠️ Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/)

### Local Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/r1anpratama/FastAPI_porject.git
   cd FastAPI_porject
   ```

2. **Configure Environment Variables:**
   Copy the example environment file and adjust if necessary.
   ```bash
   cp .env.example .env
   ```

3. **Spin up the containers:**
   ```bash
   docker-compose up -d --build
   ```

4. **Initialize Database Migrations:**
   Enter the application container and apply the initial schema.
   ```bash
   docker-compose exec web bash
   alembic revision --autogenerate -m "Initial migration"
   alembic upgrade head
   exit
   ```

## 📖 API Documentation

Once the application is running, you can access the automatic interactive API documentation:

- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Available Endpoints

- `POST /api/v1/scrape/run` - Trigger the web scraper to fetch quotes and save them to the database.
- `GET /api/v1/quotes` - Retrieve a paginated list of all scraped quotes.
- `GET /api/v1/quotes/{quote_id}` - Retrieve a specific quote by its ID.

## 📝 License

This project is open-sourced under the MIT License.
