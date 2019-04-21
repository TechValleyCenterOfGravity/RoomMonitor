#!/usr/local/bin/python

import sys
import time
from sense_hat import SenseHat
from influxdb import InfluxDBClient

sensor = SenseHat()

def get_readings(sensor):
    # Get the current temperature and humidity readings
    current_temperature = sensor.temperature
    current_humidity = sensor.humidity

    sensor.show_mesaage(current_temperature)

    return [
        {
            'measurement': 'balena-sense',
            'fields': {
                'temperature': float(current_temperature),
                'pressure': float(sensor.pressure),
                'humidity': float(current_humidity)
            }
        }
    ]

# Create the database client, connected to the influxdb container, and select/create the database
#influx_client = InfluxDBClient('influxdb', 8086, database='balena-sense')
#influx_client.create_database('balena-sense')

while True:
    measurements = get_readings(sensor)
    #influx_client.write_points(measurements)
    time.sleep(10)