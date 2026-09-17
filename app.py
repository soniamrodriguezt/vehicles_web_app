import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('Análisis de anuncios de vehículos')

# Mostrar una vista previa de los datos
st.write('Vista previa del conjunto de datos:')
st.dataframe(car_data.head())

# Histograma
if st.checkbox('Mostrar histograma'):
    st.write('Distribución del kilometraje de los vehículos')
    fig_hist = px.histogram(
        car_data,
        x='odometer',
        title='Distribución del kilometraje'
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# Gráfico de dispersión
if st.button('Mostrar gráfico de dispersión'):
    st.write('Relación entre precio y kilometraje')
    fig_scatter = px.scatter(
        car_data,
        x='odometer',
        y='price',
        title='Precio vs. kilometraje'
    )
    st.plotly_chart(fig_scatter, use_container_width=True)