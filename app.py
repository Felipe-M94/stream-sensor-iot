import streamlit as st

st.set_page_config(page_title="Dashboard IoT", page_icon="📊", layout="wide")

st.sidebar.title("📡 Monitoramento IoT")
page = st.sidebar.radio("Navegação", ["Alertas", "Tendências", "Mapa de Calor"])

if page == "Alertas":
    exec(open("pages/alerts.py").read())
elif page == "Tendências":
    exec(open("pages/trends.py").read())
elif page == "Mapa de Calor":
    exec(open("pages/heatmap.py").read())
