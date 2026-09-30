from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.core.config import settings
from app.core.database import neo4j_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    neo4j_db.verify_connection()
    yield
    # Shutdown code
    neo4j_db.close()

app = FastAPI(
    title=settings.App_name,
    version=settings.App_version,
    lifespan=lifespan
)

@app.get("/")
def root():
    return {"message": "Welcome to the GraphRAG API!"}

@app.get("/health")
def health_check():
    try:
        neo4j_db.verify_connection()
        return {"status": "healthy"}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}