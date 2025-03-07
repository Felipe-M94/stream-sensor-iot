from kafka import KafkaConsumer
import json
import os
from dotenv import load_dotenv

load_dotenv()


def get_consumer():
    return KafkaConsumer(
        os.getenv("KAFKA_TOPIC"),
        bootstrap_servers=os.getenv("KAFKA_BROKER"),
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
        auto_offset_reset="earliest",
    )
