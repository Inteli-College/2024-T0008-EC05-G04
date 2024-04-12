# Controles Periféricos 
## Introdução
A integração de sensores periféricos representa uma adição significativa à solução em desenvolvimento para o Hospital Sírio-Libanês. A inclusão do sensor infravermelho especificamente tem sido uma escolha crucial, pois eleva a confiabilidade na montagem dos kits, pois devido a esse sensor em funcionamento, quando o robô é programado para pegar um objeto em uma posição específica, podemos garantir que o objeto correto tenha sido efetivamente agarrado pelo braço mecânico. Isso se deve à capacidade do sensor de detectar a presença do objeto, conferindo uma validação adicional ao processo de montagem.

### Explicação do código (pasta *firmware*)
#### Arquivo: main.py e app.py
##### Importação das bibliotecas
```python 
# Importa o módulo urequests com o alias requests para fazer solicitações HTTP.
import urequests as requests

# Importa o módulo network para gerenciar conexões de rede.
import network

# Importa o módulo machine para interagir com o hardware do dispositivo.
import machine

# Importa o módulo time para funções relacionadas ao tempo, como pausas.
import time

# Importa um módulo personalizado chamado tokens, que contém constantes como URLs e credenciais.
import tokens
```
##### Definição da URL e funções necessárias
``` python 
# Define a URL do endpoint para enviar dados do sensor via POST.
local_url = f"{tokens.BASE_URL}/raspberry-feed"  # Substitua pela sua URL local.

# Define uma função para enviar dados do sensor para o endpoint via POST.
def send_post(distance_measured):
    # Cria um dicionário com os dados do sensor para enviar.
    payload = {"sensor_value": distance_measured}
    # Exibe o payload no console para depuração.
    print(payload)
    # Envia o payload para o endpoint e armazena a resposta.
    response = requests.post(local_url, json=payload)
    # Exibe o texto da resposta no console para depuração.
    print(response.text)

# Define a função principal que será executada quando o script for iniciado.
def main():
    # Configura um pino ADC para ler valores do sensor óptico reflexivo.
    pino_sensor = machine.ADC(26)

    # Configura dois pinos GPIO como saída, um para um LED e outro para um buzzer.
    pino_led = machine.Pin(12, machine.Pin.OUT)
    pino_buz = machine.Pin(13, machine.Pin.OUT)

    # Inicializa a interface de rede Wi-Fi como cliente.
    wlan = network.WLAN(network.STA_IF)
    # Ativa a interface de rede Wi-Fi.
    wlan.active(True)
    # Conecta à rede Wi-Fi usando as credenciais fornecidas no módulo tokens.
    wlan.connect(tokens.SSID, tokens.PASSWORD)

    # Aguarda até que a conexão Wi-Fi seja estabelecida.
    while not wlan.isconnected():
        pass
    # Informa no console que a conexão Wi-Fi foi estabelecida.
    print("Connected to wifi")

    # Inicia um loop infinito.
    while True:
        # Lê o valor atual do sensor e armazena na variável.
        distance_measured = pino_sensor.read_u16()
        # Exibe o valor medido no console para depuração.
        print(distance_measured)

        # Verifica se o valor medido está abaixo de um limiar específico.
        if distance_measured <= 25000:
            # Se estiver, exibe uma mensagem e ativa o LED e o buzzer.
            print("Objeto: Detectado")
            pino_led.on()
            pino_buz.on()
        else:
            # Se não, exibe uma mensagem e desativa o LED e o buzzer.
            print("Objeto: Ausente")
            pino_led.off()
            pino_buz.off()

        # Chama a função para enviar o valor do sensor para o endpoint.
        send_post(distance_measured)

        # Pausa a execução por um segundo antes de repetir o loop.
        time.sleep(1)
```
## Conclusão
Portanto, em conclusão este código configura o dispositivo para se conectar ao Wi-Fi, ler valores de um sensor, indicar a detecção de um objeto com um LED e um buzzer, e enviar esses valores para um servidor via HTTP POST. Assim, ele repete esse processo continuamente a cada segundo.
