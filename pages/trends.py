import streamlit as st
import plotly.express as px
from utils.database import fetch_data

st.title("📈 Tendência de Temperatura e Umidade")

query = "SELECT timestamp, sensor_id, temperature, humidity FROM sensor_data ORDER BY timestamp DESC LIMIT 500"
df = fetch_data(query)

fig = px.line(
    df,
    x="timestamp",
    y=["temperature", "humidity"],
    title="Evolução da Temperatura e Umidade",
)
st.plotly_chart(fig)
