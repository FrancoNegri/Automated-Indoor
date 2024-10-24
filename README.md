Backend for the Pecolina Greenhouse Project.

It includes:

- Docker-compose for Grafana + Influx Database
- Docker-compose for Moskito MQTT Broker
- Simple Python script that subscribes to MQTT and saves data to Influx Database

To run just run

sudo docker-compose up -d on the corresponding modules and run the pecolina_integration_servcice

Login to influx to setup database.

Once the Pecolina clients subscribes and starts sending messages you shuld start seeing the data impact in grafana.
