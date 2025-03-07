import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from utils.database import fetch_data

st.title("🔥 Mapa de Calor dos Sensores")

query = """
    SELECT sensor_id, ROUND(AVG(temperature),2) as avg_temp 
    FROM sensor_data 
    GROUP BY sensor_id 
    ORDER BY sensor_id
"""
df = fetch_data(query)

fig, ax = plt.subplots()
sns.heatmap(
    df.pivot_table(index="sensor_id", values="avg_temp"),
    cmap="coolwarm",
    annot=True,
    ax=ax,
)
ax.set_title("Temperatura Média por Sensor")

st.pyplot(fig)
