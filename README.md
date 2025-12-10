# MQTT-ITT-IT11C

- MQTT aufgaben der IT11c BS1 Traunstein in ITT

## Startup

### Mosquitto Broker starten

- Mosquitto muss installiert sein: `https://mosquitto.org/download/`
- Path: `C:\Programme\mosquitto>`
- Cmd: `.\mosquitto_sub.exe -d -t sensorclient/data -h localhost`

#### Mosquitto Broker Verbose Mode starten

- Path: `C:\Programme\mosquitto>`
- Cmd: `.\mosquitto -v`

### Sensor Client starten

- Cmd: `python sensorClient.py`
- Benötigt `paho-mqtt` Bibliothek: `pip install paho-mqtt`
