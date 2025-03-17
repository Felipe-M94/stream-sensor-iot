import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()


def get_connection():
    """Cria e retorna uma conexão com o banco de dados PostgreSQL via SQLAlchemy."""
    try:
        db_url = os.getenv("DATABASE_URL")
        if db_url is None:
            raise ValueError("DATABASE_URL environment variable is not set")
        engine = create_engine(db_url, pool_pre_ping=True)
        return engine.connect()
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None


def fetch_data(query):
    """Executa uma query no banco e retorna um DataFrame."""
    conn = get_connection()
    if conn is None:
        return None
    try:
        df = pd.read_sql(query, conn)
        return df
    except Exception as e:
        print(f"Erro ao executar query: {e}")
        return None
    finally:
        conn.close()
