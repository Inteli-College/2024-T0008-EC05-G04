# Projeto de Sensor de Proximidade para Braço Robótico

## Introdução

Este documento descreve o projeto de um sensor de proximidade integrado a um braço robótico. O sensor será montado na ponta do braço e servirá como uma forma de verificação para determinar se um item foi adequadamente agarrado pelo braço robótico. O sensor de proximidade ativará um LED e um buzzer dependendo da distância do objeto em relação ao sensor. Além disso, será exibida uma mensagem no monitor serial indicando se um objeto está sendo detectado ou não.

## Itens Utilizados

- 1 Raspberry PICO
- 1 Resistor de 220 Ohms
- 1 Resistor de 10K Ohms
- 1 LED vermelho
- 1 Buzzer
- Fios macho-macho e macho-fêmea

## Diagrama Esquemático

![Diagrama Esquemático](\img\desenho_esquematico.png)
<h6 align="center"> Fonte: Elaboração Grupo 4U </h6>

## Procedimento de Montagem

1. Conecte o LED vermelho ao Raspberry PICO, utilizando o resistor de 220 Ohms para limitar a corrente - porta GPIO 12.
2. Conecte o buzzer ao Raspberry PICO sem resistor - porta  GPIO 13.
3. Conecte o sensor de proximidade ao Raspberry PICO - porta GPIO26 para poder emitir o sinal.
4. Conecte o Raspberry PICO ao monitor serial para exibir as mensagens de detecção.

# Funcionamento

O sensor de proximidade detectará a presença de objetos próximos. Dependendo da distância, o LED vermelho será ativado e o buzzer emitirá um som. Além disso, uma mensagem será exibida no monitor serial indicando se um objeto está sendo detectado ou não.


## Código Fonte

```python
# Importação das bibliotecas necessárias
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
# Conclusão

Este projeto demonstra como utilizar um sensor de proximidade integrado a um braço robótico para verificar se um objeto foi adequadamente agarrado. Com a combinação do LED, buzzer e monitor serial, é possível obter feedback visual, auditivo e textual sobre a detecção de objetos. Este sistema pode ser útil em diversas aplicações onde a verificação de pegada é importante.
