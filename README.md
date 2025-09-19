# Indoor Monitoring Dashboard

<img width="1905" height="757" alt="image" src="https://github.com/user-attachments/assets/9851e6b3-a3be-4160-add5-5814910e2038" />

This project creates an indoor monitoring dashboard using Grafana, ESP32, and ESPHome to track temperature, humidity, and light levels.

## Overview

The setup uses an ESP32 microcontroller with ESPHome firmware to collect sensor data, which is then sent to an MQTT broker.

We use a Mosquito subscriber to then get the data from the MQTT broker to the Prometheous DB.

From there grafana takes it and uses it for the visualizations.

The service also runs Alertmanager in case you decide to create your own alerts.

This project does not use code!

Just Dockers and some magic config files to make all data flow.

## Prerequisites
- A Linux compatible host, Docker and Docker Compose
- Any ESP32 development board
- Sensors (DHT for temperature/humidity, ADC for light)
- Wi-Fi or some other way for the esp32 and host to communicate.

## Setup Instructions

### 1. ESP32 Flashing
- Clone this repository in host.
- Run the following command in the `esphome` directory:

  ```bash
  docker-compose -f up -d
- Access ESPHome at http://localhost:6052 and follow the instructions.
- Use the provided `indoor.yml` to configure the ESP32 with ESPHome.
- Update Wi-Fi credentials (`wifi_ssid`, `wifi_password`) and MQTT broker to your host IP (in this example `192.168.0.19`).
- Flash the ESP32 following the ESPHome instructions.

### 2. Setting up the Grafana Dashboard
- Clone this repository in host.
- Run the following command in the `grafana` directory:

  ```bash
  docker-compose -f up -d
- Access Grafana at http://localhost:3000 (default user: `admin`, password: `admin`).
- Import the dashboard configuration from `grafana/grafana_indor_dashboard.json` to create the dashboard.

## Usage
- Monitor real-time sensor data on the Grafana dashboard.
- Adjust `update_interval` in `esp32.json` to change data refresh rate.
- Customize alerts in `./config/alertmanager/alertmanager.yml`.

## Notes
- Ensure the MQTT broker IP and ESP32 IP match your network setup.

## Acknowledgments
- [ESPHome](https://esphome.io/) - For providing the ESPHome framework to configure and manage the ESP32.
- [Grafana](https://grafana.com/) - For the powerful dashboard and visualization tools.
- [Prometheus](https://prometheus.io/) - For the monitoring and alerting toolkit.
- [Eclipse Mosquitto](https://mosquitto.org/) - For the MQTT broker implementation.
- [Docker](https://www.docker.com/) - For containerization support.
- Special thanks to the open-source community for their contributions and support.
