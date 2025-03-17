import logging
from kafka_utils import get_consumer
from db_utils import insert_sensor_data

# Configuração do logging
LOG_FILE = "consumer.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_FILE, mode="a"),
    ],
)

consumer = get_consumer()

logging.info("Aguardando mensagens...")

for message in consumer:
    try:
        data = message.value
        logging.info(f"Recebido: {data}")

        insert_sensor_data(data)
        logging.info("Salvo no banco com sucesso!")

    except Exception as e:
        logging.error(f"Erro ao processar mensagem: {e}", exc_info=True)
