# Indoor Monitoring Dashboard

<img width="1905" height="757" alt="image" src="https://github.com/user-attachments/assets/9851e6b3-a3be-4160-add5-5814910e2038" />

This project creates an indoor monitoring dashboard using Grafana, ESP32, and ESPHome to track temperature, humidity, and light levels, leveraging real-time data collection, MQTT-based communication, and Prometheus for storage and visualization. The setup integrates an ESP32 microcontroller configured with ESPHome to gather sensor data, which is then transmitted via MQTT to a local broker. Grafana provides an intuitive interface to display this data in customizable dashboards, making it easy to monitor environmental conditions over time.

The system is designed for flexibility and scalability, utilizing Docker containers to manage services like the MQTT broker, Prometheus, and Grafana. This containerized approach simplifies deployment and ensures consistent performance across different environments. Users can adjust sensor update intervals and thresholds directly in the ESPHome configuration or fine-tune the dashboard layout in Grafana, tailoring the setup to specific needs such as home automation or environmental research.

Additionally, the project includes alerting capabilities through Alertmanager, allowing users to set notifications for unusual conditions, such as extreme temperature changes. The open-source nature of the tools ensures ongoing support and community-driven improvements, while the included Docker Compose files streamline the setup process for both beginners and experienced developers. This combination of hardware and software creates a robust solution for indoor monitoring, adaptable to various use cases.

## Data Flow Overview
1. **Data Collection**: The ESP32, configured with ESPHome, collects sensor data (temperature, humidity, and light) using a DHT sensor and an ADC pin.
2. **MQTT Transmission**: The collected data is published to the MQTT broker (Eclipse Mosquitto).
3. **Data Processing**: The MQTT broker forwards the data to MQTT exporters (e.g., `kpetrem/mqtt-exporter` and `sapcc/mosquitto-exporter`), which convert it into a format compatible with Prometheus.
4. **Data Storage**: Prometheus scrapes the data from the MQTT exporters and stores it in a time-series database.
5. **Visualization**: Grafana pulls the stored data from Prometheus and displays it on a dashboard.
6. **Alerting (Optional)**: AlertManager, integrated with Prometheus, can be configured to send notifications based on predefined thresholds.

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
