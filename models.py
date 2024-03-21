from sqlalchemy import Column, Integer, String, Date, DateTime, Float, DECIMAL
from database import Base

class Gasto(Base):
    __tablename__ = 'gastos'
    __table_args__ = {'schema': 'home'}

    fecha = Column(Date, nullable=False)
    importe = Column(DECIMAL(10, 2), primary_key=True, nullable=False)
    categoria = Column(String, nullable=False)
    subcategoria = Column(String, nullable=False)
    formapago = Column(String, nullable=False)
    tarjeta = Column(String)
    cuotas = Column(Integer)
    fechacarga = Column(DateTime, primary_key=True, nullable=False)