import os
import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configuração do banco de dados
DB_PARAMS = {
    "dbname": os.getenv("DB_NAME", "sensor_data"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", ""),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "5432")),
}


def get_data():
    """Consulta os dados do PostgreSQL."""
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        query = "SELECT timestamp, sensor_id, temperature, humidity FROM sensor_data ORDER BY timestamp DESC LIMIT 100;"
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Erro ao conectar ao banco: {e}")
        return pd.DataFrame()


# Interface do Streamlit
st.title("Monitoramento de Sensores - Alertas Críticos")

# Carregar dados
df = get_data()

if not df.empty:
    # Definir limites críticos
    temp_critica = 35.0
    umidade_critica = 40.0

    df["alerta"] = df.apply(
        lambda x: (x["temperature"] >= temp_critica)
        or (x["humidity"] <= umidade_critica),
        axis=1,
    )

    # Gráfico interativo
    fig = px.scatter(
        df,
        x="timestamp",
        y="temperature",
        color="alerta",
        color_discrete_map={True: "red", False: "blue"},
        title="Temperatura ao longo do tempo (Alerta em vermelho)",
    )
    st.plotly_chart(fig)

    # Exibir registros críticos
    st.subheader("Registros Críticos")
    st.dataframe(df[df["alerta"] == True])
else:
    st.warning("Nenhum dado disponível.")
