import urequests as requests
import network
from machine import Pin
from time import sleep

import tokens

# Pino GPIO conectado ao sensor óptico reflexivo
pino_sensor = machine.ADC(26)

# Pino GPIO conectado ao LED
pino_led = machine.Pin(12, machine.Pin.OUT)
pino_buz = machine.Pin(13, machine.Pin.OUT)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(tokens.SSID, tokens.PASSWORD)

while not wlan.isconnected():
    pass
print("Connected to wifi")

# URL do endpoint local para enviar o POST
local_url = '{url}/raspberry'  # Replace with your local URL

# Função para enviar o POST com o valor do sensor
def send_post(distance_measured):
    payload = {'sensor_value': distance_measured}
    try:
        response = requests.post(local_url, json=payload)
        print('Response:', response.text)
    except Exception as e:
        print('Error:', e)

while True:
    distance_measured = pino_sensor.read_u16()
    print(distance_measured)

    if distance_measured <= 25000:  
        print("Objeto: Detectado")
        pino_led.on()
        pino_buz.on()
    else:
        print("Objeto: Ausente")
        pino_led.off()
        pino_buz.off()

    # Send the sensor value to the local URL
    send_post(distance_measured)

    utime.sleep(1)