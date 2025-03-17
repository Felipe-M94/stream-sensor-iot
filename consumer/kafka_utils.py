from math import e
from flask import g
from kafka import KafkaConsumer
import json
import os
from dotenv import load_dotenv

load_dotenv()


def get_consumer():
    return KafkaConsumer(
        os.getenv("KAFKA_TOPIC"),
        bootstrap_servers=os.getenv("KAFKA_BROKER"),
        group_id=os.getenv("KAFKA_GROUP_ID"),
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
        auto_offset_reset="earliest",
        enable_auto_commit=True,
    )
