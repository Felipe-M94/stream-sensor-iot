import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()


def get_connection():
    """Cria e retorna uma conexão com o banco de dados PostgreSQL."""
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
        )
        return conn
    except psycopg2.OperationalError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None


def fetch_data(query):
    """Executa uma query no banco e retorna um DataFrame."""
    conn = get_connection()
    if conn is None:
        return None
    try:
        df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        print(f"Erro ao executar query: {e}")
        return None
    finally:
        conn.close()
