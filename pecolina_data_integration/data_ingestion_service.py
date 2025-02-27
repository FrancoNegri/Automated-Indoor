import json
import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# Configuration
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "garden/sensors"
INFLUXDB_ADDRESS = "192.168.0.19:8086"
token = "yZJRrtVvV6Tv9NnhmnOLe9iCR43fP-tmPBNaZyZ1d9Heac2hGc3NISit-i8Ol_7uIOr5MiOKxFaAxzvSeQdqsg=="
org = "Peco"
bucket = "garden_data"

# InfluxDB client setup
influxdb_client = InfluxDBClient(url=INFLUXDB_ADDRESS ,token=token,org=org)
write_api = influxdb_client.write_api(write_options=SYNCHRONOUS)

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with result code {rc}")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic} msg: {repr(msg.payload)}")
    try:
	# Decode and parse JSON
        payload = msg.payload.decode("utf-8")
        data = json.loads(payload)
        write_to_influxdb(data)
    except Exception as e:
        print(f"Error processing message: {e}")

def write_to_influxdb(data):
    point = Point("measurement1").tag("location", "").field("temperature", data["temperature"]).field("humidity", data["humidity"]).field("lightLevel", data["lightLevel"]).field("soilMoisture", data["soilMoisture"])
    write_api.write(bucket=bucket, org="Peco", record=point)

def main():
    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    mqtt_client.loop_forever()

if __name__ == "__main__":
    main()

