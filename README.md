📡 Industrial IoT Sensor Simulation Project
📌 Project Overview

This project simulates Industrial IoT (IIoT) sensor data transmission using three different communication protocols:

MQTT

CoAP

OPC UA

Each protocol sends simulated temperature and humidity data to a corresponding server endpoint. The goal of this project is to compare how different industrial communication protocols operate and how they handle sensor data transmission.

🗂 Project Structure
project-folder/
│
├── mqtt_sensor_simulation.py
├── coap_sensor_simulation.py
├── opcua_sensor_simulation.py
├── coap_server.py
├── data_visualization.py
└── README.md
🛠 Requirements
Python Version

Python 3.10+

Required Libraries

Install all required packages:

pip install paho-mqtt aiocoap opcua matplotlib pandas
🔹 Protocol 1: MQTT
Description

Simulates a sensor publishing temperature and humidity data to an MQTT broker.

Default Settings

Broker: localhost

Port: 1883

Topic: sensor/data

🟢 How to Run MQTT
Step 1: Start MQTT Broker (Mosquitto)

Open a terminal and run:

mosquitto

Leave this running.

Step 2: Run MQTT Sensor Simulation

Open a new terminal:

python mqtt_sensor_simulation.py

You should see data being published every second.

🔹 Protocol 2: CoAP
Description

Simulates a sensor sending data using the CoAP protocol.

CoAP requires a server running on port 5683.

🟢 How to Run CoAP
Step 1: Start CoAP Server
python coap_server.py

You should see:

CoAP server running on coap://localhost:5683/sensor/data

Leave this running.

Step 2: Run CoAP Sensor Simulation

Open another terminal:

python coap_sensor_simulation.py

The server terminal will display received sensor data.

🔹 Protocol 3: OPC UA
Description

Simulates a sensor sending data using OPC UA protocol.

🟢 How to Run OPC UA
Step 1: Start OPC UA Server

If your project includes a server script, run:

python opcua_server.py
Step 2: Run OPC UA Sensor Simulation
python opcua_sensor_simulation.py
📊 Data Visualization

The project includes a visualization script to display collected sensor data.

Run:

python data_visualization.py

This will generate a graph showing temperature and humidity trends.

⚙️ How the Simulation Works

Each sensor script:

Generates random temperature values between 20–25°C

Generates random humidity values between 30–50%

Packages the data as JSON

Sends the data to the respective protocol endpoint

Repeats every second

Example payload:

{
  "temperature": 22.4,
  "humidity": 41.8
}
🔍 Troubleshooting
Error: ModuleNotFoundError

Install missing packages:

pip install package_name
Error: MQTT Connection Refused

Make sure Mosquitto broker is running:

mosquitto
Error: CoAP NetworkError

Make sure CoAP server is running before starting the client:

python coap_server.py
📈 Learning Objectives

This project demonstrates:

Differences between MQTT, CoAP, and OPC UA

Publisher/Subscriber architecture (MQTT)

REST-based lightweight communication (CoAP)

Industrial automation protocol structure (OPC UA)

Handling asynchronous networking in Python
