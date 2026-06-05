from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field
class Settings(BaseSettings):
    # Nombre de tu API
    PROJECT_NAME: str = "Sistema de Reservas"

    DB_USER: str
    DB_PW: str
    DB_HOST: str
    DB_PORT: int
    DB_SCHEMA: str
    
    # URL de conexión a la base de datos.
    # Al estar usando FastAPI (asíncrono) y PostgreSQL, el driver ideal es 'asyncpg'.
    # Formato: postgresql+asyncpg://usuario:password@host:puerto/nombre_bd
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PW}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_SCHEMA}"

    # Configuración de Pydantic para que lea automáticamente un archivo .env si existe en la raíz
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

# Instanciamos la configuración para poder importarla en otros archivos como 'settings.DATABASE_URL'
settings = Settings()