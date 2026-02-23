import paho.mqtt.client as mqtt
import random
import time
import json

broker = "localhost"
port = 1883
topic = "sensor/data"

client = mqtt.Client()
client.connect(broker, port)

def simulate_sensor_data():
    while True:
        temperature = round(random.uniform(20.0, 25.0), 2)
        humidity = round(random.uniform(30.0, 50.0), 2)

        payload = {
            "temperature": temperature,
            "humidity": humidity
        }

        client.publish(topic, json.dumps(payload))
        print("Published:", payload)

        time.sleep(1)

simulate_sensor_data()