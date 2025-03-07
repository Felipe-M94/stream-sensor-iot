import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
    )


def insert_sensor_data(data):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO sensor_data (sensor_id, resource_id, temperature, humidity, timestamp) 
        VALUES (%s, %s, %s, %s, %s)
    """,
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
