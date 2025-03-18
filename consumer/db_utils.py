from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import os
from dotenv import load_dotenv
from urllib.parse import urlparse

# Carregar variáveis de ambiente
load_dotenv()


def get_connection():
    """Cria e retorna um engine do SQLAlchemy para conexão com PostgreSQL."""
    try:
        db_url = os.getenv("DATABASE_URL")
        if db_url is None:
            raise ValueError("DATABASE_URL environment variable is not set")

        parsed_url = urlparse(db_url)
        query_params = parsed_url.query

        if "sslmode" not in query_params:
            db_url = (
                f"{db_url}&sslmode=require"
                if query_params
                else f"{db_url}?sslmode=require"
            )

        engine = create_engine(db_url, pool_pre_ping=True)
        return engine
    except SQLAlchemyError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None


def insert_sensor_data(data):
    """Insere os dados do sensor no banco de dados."""
    engine = get_connection()
    if engine is None:
        return

    try:
        with engine.connect() as conn:
            query = text(
                """
                INSERT INTO sensor_data (sensor_id, resource_id, temperature, humidity, timestamp) 
                VALUES (:sensor_id, :resource_id, :temperature, :humidity, :timestamp)
            """
            )

            conn.execute(query, data)

    except SQLAlchemyError as e:
        print(f"Erro ao inserir dados: {e}")
