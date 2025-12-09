import time
import random
import json
import paho.mqtt.client as mqtt

class SensorClient:
    def __init__(self):
        try:
            config_file = open("config.txt")
            self.room = config_file.readline().rstrip()
            self.brokerIP = config_file.readline().rstrip()
            self.interval = int(config_file.readline().rstrip())
            config_file.close()
            
            self.temp = 25
            self.humidity = 81
            
            try:
                f = open("limits.txt")
                self.templimit = int(f.readline().rstrip())
                self.humiditylimit = int(f.readline().rstrip())
                f.close()
            except:
                self.templimit = 65.0
                self.humiditylimit = 85.0
            
            self.client = mqtt.Client()
            self.client.on_message = self.messageReceived
            
        except Exception as e:
            print("Config file missing or invalid, client will shut down")
            print(f"Error: {e}")
            return

        print("Sensor Client is running:")
        print("Room: " + self.room)
        print("Time interval for data push: " + str(self.interval))
        print("Broker IP: " + self.brokerIP)
        print("Temp: " + str(self.temp))
        print("Humidity: " + str(self.humidity))
        print("Temp - limit: " + str(self.templimit))
        print("Humid - limit: " + str(self.humiditylimit))

    def readDataFromSensor(self):
        """liest die Sensordaten"""

        self.temp = round(random.uniform(18.0, 25.0), 1)
        self.humidity = round(random.uniform(30.0, 60.0), 1)

    def statusInfo(self):
        """generiert einen String für eine Statusmeldung"""
        # Format: room:temp:humid:templimit:humiditylimit
        return f"{self.room}:{self.temp}:{self.humidity}:{self.templimit}:{self.humiditylimit}"

    def run(self):
        """Endlosschleife für Sensoren auslesen -> Daten senden"""
        print(f"Verbinde mit Broker {self.brokerIP}...")
        try:
            self.client.connect(self.brokerIP, 1883, 60)
            self.client.loop_start() 

            while True:
                self.readDataFromSensor()
                message = self.statusInfo()
                topic = f"home/{self.room}/status"
                
                self.client.publish(topic, message)
                print(f"Gesendet: {message} an {topic}")
                
                time.sleep(self.interval)
                
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")
        finally:
            self.client.loop_stop()
            self.client.disconnect()

    def messageReceived(self, client, userdata, message):
        """Mqtt Message wurde erhalten"""
        print(f"Nachricht empfangen: {message.payload.decode()} auf Topic {message.topic}")

if __name__ == "__main__":
    sensor = SensorClient()
    if hasattr(sensor, 'room'):
        sensor.run()
