from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    App_name: str = "GraphRAG API"
    App_version: str = "0.1.0"

    NEO4J_URI: str
    NEO4J_USER: str
    NEO4J_PASSWORD: str

    GROQ_API_KEY: str
    GROQ_MODEL: str

    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()