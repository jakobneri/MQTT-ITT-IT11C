import paho.mqtt.client as mqtt
import time

class sensorClient():

    def __init__(self, room, brokerIP, interval, temp, humidity):
        self.room = room
        self.brokerIP = brokerIP
        self.interval = interval
        self.temp = temp
        self.humidity = humidity

    def redDataFromSensor(self):
        return {
            mqtt.topic: f"home/{self.room}/sensor",
            mqtt.payload: {
                "temperature": self.temp,
                "humidity": self.humidity,
                "interval": self.interval
        }
            }
    
    def statusInfo(self):
        return str({
            "room": self.room,
            "brokerIP": self.brokerIP,
            "interval": self.interval,
            "temperature": self.temp,
            "humidity": self.humidity})
    
    def run(self):
        while True:
            data = self.redDataFromSensor()
            print(f"Publishing data to {data[mqtt.topic]}: {data[mqtt.payload]}")
            self.statusInfo()
            time.sleep(self.interval)  

    def messageRecieved():
        print("Message received from MQTT.")

    