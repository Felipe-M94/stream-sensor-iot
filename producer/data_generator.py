import random
import time


def generate_sensor_data():
    return {
        "sensor_id": f"sensor_{random.randint(1, 10)}",
        "resource_id": f"res_{random.randint(100, 200)}",
        "temperature": round(random.uniform(20, 50), 2),
        "humidity": round(random.uniform(30, 90), 2),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
