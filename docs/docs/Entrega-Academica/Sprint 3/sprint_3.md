# Sprint 3
Nesta sprint focamos no aprimoramento de dos movimento do robô, além disso também houve a adição de controles periféricos.

## Computação:
Houve a adição de um sensor infravermelho de proximidade integrado a um braço robótico. O sensor será montado na ponta do braço e servirá como uma forma de verificação para determinar se um item foi adequadamente agarrado pelo braço robótico. O sensor de proximidade ativará um LED e um buzzer dependendo da distância do objeto em relação ao sensor. Além disso, será exibida uma mensagem no monitor serial indicando se um objeto está sendo detectado ou não.

Os itens utilizados no projeto incluem 1 Raspberry PICO, 1 resistor de 220 Ohms, 1 resistor de 10K Ohms, 1 LED vermelho, 1 buzzer e fios macho-macho e macho-fêmea.

O funcionamento do sensor de proximidade consiste em detectar a presença de objetos próximos. Dependendo da distância, o LED vermelho será ativado e o buzzer emitirá um som. Além disso, uma mensagem será exibida no monitor serial indicando se um objeto está sendo detectado ou não.

O código-fonte apresentado configura o funcionamento do sensor, controlando o LED e o buzzer com base na leitura do sensor. O projeto destina-se a verificar se um objeto foi adequadamente agarrado pelo braço robótico, fornecendo feedback visual, auditivo e textual sobre a detecção de objetos.

Além disso, o texto descreve uma API de Gerenciamento de Kits, fornecendo uma série de endpoints para manipular kits, posições de kits, registro de usuários e itens, e consultas relacionadas. Os endpoints incluem funcionalidades como consultar kits, adicionar novos kits, registrar usuários, autenticar login, criar posições de kit, registrar itens, consultar posições de kit, consultar itens, criar pedidos de kit, consultar pedidos de kit, atualizar status de pedidos de kit e consultar pedidos de kit por status. Cada endpoint tem uma descrição detalhada de sua função, parâmetros de requisição e resposta, e código de status HTTP correspondente. O texto destaca a organização e eficiência da API para gerenciar dados relacionados a kits de forma abrangente.