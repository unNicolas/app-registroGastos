import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import SessionLocal
from models import Gasto
from datetime import datetime
from functions import check_database_connection

# Título del formulario
st.title('Registro de Gastos')

# Widgets para ingresar datos
fecha = st.date_input('Fecha del Gasto', value=None, min_value=None, max_value=None, key=None)
print(fecha)
categoria = {
'Alimentación': ['Supermercado', 'Verdulería', 'Carnicería', 'Snacks'],
'Transporte': ['Reparación Auto', 'Mejoras Auto', 'Combustible', 'Peaje', 'Multas', 'Impuestos'],
'Entretenimiento': ['Fiestitas', 'Complementos fiestitas', 'Viajes', 'Resto', 'Delivery', 'Bailes', 'Boliches', 'Otros'],
'Vestimenta':['Compra Ropa', 'Calzado', 'Reparación'],
'Hogar': ['Reparaciones', 'Mejoras', 'Mobiliario', 'Limpieza'],
'Cuidado Personal':['Proteina', 'Creatina', 'Vitaminas', 'Skin Care', 'Otros Suplementos'],
'Otros':[] # Actualmente no hay subcategorías
}

selected_categoria = st.selectbox('Selecciona una Categoría:', list(categoria.keys()))

#Verificar si es Otros, ya que no tiene subcategoría
if selected_categoria !='Otros':
    #En base a la categoría escogida busca las sub disponibles
    subcategoria = categoria[selected_categoria]
    #Crea un selectbox para las subcategorías
    selected_subcategoria = st.selectbox('Selecciona una Subcategoría:', subcategoria)
else:
    selected_subcategoria = None

importe = st.number_input('Importe del Gasto', min_value=0.0, step=0.01)
medio_pago = st.selectbox('Medio de Pago', ['Efectivo', 'Transferencia', 'Tarjeta de Crédito', 'Tarjeta de Débito'])

# Opción para cuotas en caso de elegir Tarjeta de Crédito
if medio_pago == 'Tarjeta de Crédito':
    tarjeta = st.selectbox('Tarjeta de Crédito', ['Santander Visa', 'Santander Mastercard', 'Galicia Visa', 'Galicia Mastercard'])
    cuotas = st.number_input('Cantidad de Cuotas', min_value=1, max_value=12, step=1)


fecha_carga = datetime.now()
# Botón para guardar
if st.button('Guardar Gasto'):
    # Verificar la conexión con la base de datos antes de intentar guardar
    if check_database_connection():
        # Conexión exitosa, proceder con el guardado del gasto
        try:
             with SessionLocal() as db:
                 nuevo_gasto = Gasto(
                    fecha=fecha,
                    importe=importe,
                    categoria=selected_categoria,
                    subcategoria=selected_subcategoria,
                    formapago=medio_pago,
                    tarjeta=tarjeta if medio_pago == 'Tarjeta de Crédito' else None,  # Solo se guarda la tarjeta si se elige Tarjeta de Crédito
                    cuotas=cuotas if medio_pago == 'Tarjeta de Crédito' else None,  # Solo se guardan las cuotas si se elige Tarjeta de Crédito
                    fechacarga = fecha_carga
                    )
                    # Agregar el nuevo gasto a la sesión
                 db.add(nuevo_gasto)
                # Confirmar los cambios en la base de datos
                 db.commit()
                 st.success('¡Gasto registrado exitosamente!')
        except Exception as e:
            st.error(f"Error al guardar el gasto: {e}")
    else:
        st.error("No se pudo conectar con la base de datos. Inténtalo de nuevo más tarde.")


