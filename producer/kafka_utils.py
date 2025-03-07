from kafka import KafkaProducer
import json
import os
from dotenv import load_dotenv

load_dotenv()


def get_producer():
    return KafkaProducer(
        bootstrap_servers=os.getenv("KAFKA_BROKER"),
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )
