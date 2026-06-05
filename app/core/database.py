from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.core.config import settings

# El engine gestiona el pool de conexiones hacia PostgreSQL.
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,          # Imprime las consultas SQL generadas en la consola (útil para debug en desarrollo)
    pool_pre_ping=True, # Verifica que la conexión esté viva antes de usarla, evitando errores de desconexión
)

# Genera las sesiones que usaremos para realizar las consultas (SELECT, INSERT, etc.)
SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False, # Importante en asíncrono: permite acceder a los atributos del modelo después de hacer un commit sin tener que hacer otra consulta
    autocommit=False,
    autoflush=False
)