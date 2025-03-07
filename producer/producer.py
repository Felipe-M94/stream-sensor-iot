import time
from data_generator import generate_sensor_data
from kafka_utils import get_producer

producer = get_producer()
topic = "sensor_data"

while True:
    data = generate_sensor_data()
    producer.send(topic, data)
    print(f"Enviado: {data}")
    time.sleep(1)  # Enviar a cada 5 segundos
