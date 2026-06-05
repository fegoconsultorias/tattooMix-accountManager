import asyncio
from sqlalchemy import text
from app.core.database import engine

async def test_connection():
    try:
        # Iniciamos una conexión asíncrona con la base de datos
        async with engine.begin() as conn:
            # Ejecutamos una consulta SQL pura y muy simple
            result = await conn.execute(text("SELECT * FROM clients c;"))
            
            # Si logramos obtener el resultado, la conexión es un éxito
            print("✅ ¡Conexión exitosa a PostgreSQL!")
            print("Resultado de la consulta:", result.scalar())
            
    except Exception as e:
        print("❌ Error al conectar con la base de datos:")
        print(e)
    finally:
        # Es buena práctica cerrar el motor al terminar el script
        await engine.dispose()

if __name__ == "__main__":
    # Ejecutamos la función asíncrona usando asyncio
    asyncio.run(test_connection())