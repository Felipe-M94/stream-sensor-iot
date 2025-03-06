import json
import time
import random
from kafka import KafkaProducer

# Configuração do Kafka
KAFKA_SERVER = "localhost:9094"
TOPIC_NAME = "sensor_data"

# Inicializando o produtor Kafka
producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    retries=5,
    acks="all",
)


def generate_sensor_data():
    """Gera dados aleatórios para simular sensores IoT."""
    sensor_id = f"sensor_{random.randint(1, 5)}"
    resource_id = f"machine_{random.randint(1, 3)}"
    temperature = round(random.uniform(20.0, 40.0), 2)
    humidity = round(random.uniform(30.0, 90.0), 2)

    return {
        "sensor_id": sensor_id,
        "resource_id": resource_id,
        "temperature": temperature,
        "humidity": humidity,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    }


# Enviando dados continuamente
try:
    while True:
        sensor_data = generate_sensor_data()
        future = producer.send(TOPIC_NAME, value=sensor_data)
        result = future.get(timeout=10)
        print(f"Enviado: {sensor_data}")
        time.sleep(1)  # Envia um novo dado a cada 1 segundo
except Exception as e:
    print(f"Erro ao enviar dados: {e}")
finally:
    producer.flush()
    producer.close()
