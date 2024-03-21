from sqlalchemy import text
from database import SessionLocal

def check_database_connection(retries=3, delay=1):
    for _ in range(retries):
        try:
            # Intenta crear una sesión y ejecutar una consulta simple
            
            with SessionLocal() as db:
                db.execute(text("SELECT 1"))  # Corregir aquí
            # Si la consulta se ejecuta correctamente, la base de datos está accesible
            return True
        except Exception as e:
            print(f"Error al conectar con la base de datos: {e}")
            # Espera un breve período de tiempo antes de realizar un nuevo intento
            time.sleep(delay)
    # Si después de los intentos especificados la base de datos no está accesible, retorna False
    return False




