import os
import json
import logging
import psycopg2
from kafka import KafkaConsumer
from psycopg2 import OperationalError
from dotenv import load_dotenv

load_dotenv()

# Configuração do logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


TOPIC_NAME = "sensor_data"
KAFKA_SERVER = os.getenv("KAFKA_SERVER", "localhost:9094")


DB_PARAMS = {
    "dbname": os.getenv("DB_NAME", "sensor_data"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", ""),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "5432")),
}

# Conectar ao Kafka
try:
    consumer = KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=KAFKA_SERVER,
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
        auto_offset_reset="earliest",
    )
    logging.info("Conectado ao Kafka.")
except Exception as e:
    logging.error(f"Erro ao conectar ao Kafka: {e}")
    exit(1)


def get_db_connection():
    """Tenta conectar ao PostgreSQL, com tentativas automáticas em caso de falha."""
    retries = 5
    for attempt in range(retries):
        try:
            conn = psycopg2.connect(**DB_PARAMS)
            return conn
        except OperationalError as e:
            logging.warning(
                f"Tentativa {attempt + 1}/{retries} - Erro ao conectar ao DB: {e}"
            )

    logging.error("Falha ao conectar ao banco de dados após várias tentativas.")
    exit(1)


def create_table():
    """Cria a tabela no PostgreSQL caso ela não exista."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS sensor_data (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMPTZ DEFAULT now(),
            sensor_id TEXT,
            resource_id TEXT,
            temperature FLOAT,
            humidity FLOAT
        )
    """
    )
    conn.commit()
    cur.close()
    conn.close()
    logging.info("Tabela verificada/criada no PostgreSQL.")


def process_messages():
    """Consome mensagens do Kafka e insere no banco de dados."""
    logging.info("Aguardando mensagens...")

    for message in consumer:
        try:
            data = message.value
            logging.info(f"Recebido: {data}")

            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO sensor_data (sensor_id, resource_id, temperature, humidity, timestamp) VALUES (%s, %s, %s, %s, %s)",
                (
                    data["sensor_id"],
                    data["resource_id"],
                    data["temperature"],
                    data["humidity"],
                    data["timestamp"],
                ),
            )
            conn.commit()
            cur.close()
            conn.close()
            logging.info("Dados salvos com sucesso.")
        except Exception as e:
            logging.error(f"Erro ao processar mensagem: {e}")


if __name__ == "__main__":
    create_table()
    process_messages()
