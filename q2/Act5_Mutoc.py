from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass


class PHSensor(Sensor):
    def get_reading(self):
        print("[pH sensor] reading: 7.2 pH (neutral)")


class TempSensor(Sensor):
    def get_reading(self):
        print("[temperature sensor] reading: 24.5°C")


print("--- Lab Inventory System ---")

ph_sensor = PHSensor()
temp_sensor = TempSensor()

ph_sensor.get_reading()
temp_sensor.get_reading()

print("\n----------------------------")


