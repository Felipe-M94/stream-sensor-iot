from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()


def get_connection():
    """Cria e retorna uma conexão com o banco de dados PostgreSQL via SQLAlchemy."""
    try:
        db_url = os.getenv("DATABASE_URL")
        if db_url is None:
            raise ValueError("DATABASE_URL environment variable is not set")
        db_url += "?sslmode=require"
        if db_url is None:
            raise ValueError("DATABASE_URL environment variable is not set")
        engine = create_engine(db_url, pool_pre_ping=True)
        return engine.connect()
    except SQLAlchemyError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None


def insert_sensor_data(data):
    """Insere os dados do sensor no banco de dados."""
    conn = get_connection()
    if conn is None:
        return
    try:
        from sqlalchemy.sql import text

        query = text(
            """
            INSERT INTO sensor_data (sensor_id, resource_id, temperature, humidity, timestamp) 
            VALUES (:sensor_id, :resource_id, :temperature, :humidity, :timestamp)
        """
        )
        conn.execute(
            query,
            {
                "sensor_id": data["sensor_id"],
                "resource_id": data["resource_id"],
                "temperature": data["temperature"],
                "humidity": data["humidity"],
                "timestamp": data["timestamp"],
            },
        )
        conn.commit()
    except SQLAlchemyError as e:
        print(f"Erro ao inserir dados: {e}")
    finally:
        conn.close()
