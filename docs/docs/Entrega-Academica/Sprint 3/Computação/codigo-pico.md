# Raspberry Pi

Raspberry Pi é uma série de mini-computadores de placa única multiplataforma, de tamanho reduzido com componentes integrados, que se conecta a um monitor de computador ou televisão, e usa um teclado e um mouse padrão.

# Código Pico

## Importação das bibliotecas necessárias
from machine import Pin, ADC  # Importa as classes Pin e ADC da biblioteca machine para controle dos pinos e conversão analógico-digital
import utime  # Importa a biblioteca utime para manipulação de tempo

## Pino GPIO conectado ao sensor óptico reflexivo
pino_sensor = ADC(26)  # Cria um objeto ADC para ler a entrada analógica do pino GPIO 26, que está conectado ao sensor

# Pino GPIO conectado ao LED

# Importação das bibliotecas necessárias
```python
from machine import Pin, ADC  # Importa as classes Pin e ADC da biblioteca machine para controle dos pinos e conversão analógico-digital
import utime  # Importa a biblioteca utime para manipulação de tempo

# Pino GPIO conectado ao sensor óptico reflexivo
pino_sensor = ADC(26)  # Cria um objeto ADC para ler a entrada analógica do pino GPIO 26, que está conectado ao sensor

# Pino GPIO conectado ao LED
pino_led = Pin(12, Pin.OUT)  # Cria um objeto Pin para controlar o pino GPIO 12 como saída, conectado ao LED
pino_buz = Pin(13, Pin.OUT)
# Loop principal
while True:
    # Ler o estado do pino do sensor
    estado_sensor = pino_sensor.read_u16()  # Lê o valor analógico do sensor e armazena em estado_sensor
    print(estado_sensor)  # Imprime o valor do sensor

    # Controlar o LED com base no estado do sensor
    if estado_sensor <= 25000:  # Se o valor do sensor for menor ou igual a 62000
        print("Objeto: Detectado")  # Imprime uma mensagem indicando que um objeto foi detectado
        pino_led.on()  # Ligar o LED, acionando o pino conectado ao LED
        pino_buz.on()  # Ligar o Buzzer, acionando o pino conectado ao Buzzer
    else:  # Caso contrário
        print("Objeto: Ausente")  # Imprime uma mensagem indicando que nenhum objeto foi detectado
        pino_led.off()  # Desligar o LED, desativando o pino conectado ao LED
        pino_buz.off()  # Desligar o Buzzer, desativando o pino conectado ao Buzzer 

    # Aguardar um curto período de tempo antes de verificar novamente
    utime.sleep(1)  # Espera por 1 segundo antes de repetir o loop para evitar leituras muito frequentes
```

