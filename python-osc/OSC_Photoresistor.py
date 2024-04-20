from gpiozero import LightSensor
from time import sleep

ldr = LightSensor(25)  # alter if using a different pin
while True:
    print(ldr.value)
    sleep(1)