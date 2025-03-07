import streamlit as st
import plotly.express as px
from utils.database import fetch_data

st.title("Alertas Criticos")

query = """
    SELECT timestamp, sensor_id, temperature, humidity 
    FROM sensor_data 
    WHERE temperature > 40 OR humidity > 80
    ORDER BY timestamp DESC
    LIMIT 100
"""
df = fetch_data(query)

fig = px.scatter(
    df,
    x="timestamp",
    y="temperature",
    color="sensor_id",
    title="Alertas de Temperatura Critica",
)
st.plotly_chart(fig)
