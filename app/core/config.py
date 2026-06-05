from pydantic_settings import BaseSettings, SettingsConfigDict

import os
from dotenv import load_dotenv

# 1. Load base configuration first
load_dotenv(".env")

# Access variables normally
DB_USER = os.getenv("DB_USER")
DB_PW = os.getenv("DB_PW")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_SCHEMA = os.getenv("DB_SCHEMA")

class Settings(BaseSettings):
    # Nombre de tu API
    PROJECT_NAME: str = "Sistema de Reservas"
    
    # Configuración de Pydantic para que lea automáticamente un archivo .env si existe en la raíz
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # URL de conexión a la base de datos.
    # Al estar usando FastAPI (asíncrono) y PostgreSQL, el driver ideal es 'asyncpg'.
    # Formato: postgresql+asyncpg://usuario:password@host:puerto/nombre_bd
    DATABASE_URL: str = f"postgresql+asyncpg://{DB_USER}:{DB_PW}@{DB_HOST}:{DB_PORT}/{DB_SCHEMA}"


# Instanciamos la configuración para poder importarla en otros archivos como 'settings.DATABASE_URL'
settings = Settings()