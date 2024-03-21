import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener las variables de entorno
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')

# Cadena de conexión a la base de datos
SQLALCHEMY_DATABASE_URI = f"mssql+pymssql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Crear una instancia de motor de SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# Crear una sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

