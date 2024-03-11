import urequests as requests
import network
from machine import Pin
from time import sleep

import tokens

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(tokens.SSID, tokens.PASSWORD)

while not wlan.isconnected():
    pass
print("Connected to wifi")

button = Pin(20, Pin.IN, Pin.PULL_UP)

while True:
    response = requests.post(f"{tokens.BASE_URL}/echo", json={"value": button.value()})
    print(response.text)
    sleep(1)
