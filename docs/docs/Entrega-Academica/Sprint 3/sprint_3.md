# Sprint 3
Nesta sprint, o foco foi no aprimoramento dos movimentos do robô, além da adição de controles periféricos.

## Computação
Foi adicionado um sensor infravermelho de proximidade a um braço robótico. Este sensor, montado na ponta do braço, serve como um mecanismo de verificação para determinar se um item foi adequadamente agarrado pelo braço robótico. Dependendo da distância do objeto em relação ao sensor, um LED e um buzzer são ativados. Além disso, uma mensagem é exibida no monitor serial, indicando se um objeto está sendo detectado ou não.

Os componentes utilizados no projeto incluem um Raspberry PICO, um resistor de 220 Ohms, um resistor de 10K Ohms, um LED vermelho, um buzzer e fios macho-macho e macho-fêmea.

A funcionalidade do sensor de proximidade é detectar a presença de objetos próximos. Conforme a distância, o LED vermelho acende e o buzzer emite um som. Simultaneamente, uma mensagem é mostrada no monitor serial, informando sobre a detecção de um objeto.

O código-fonte elaborado configura a operação do sensor, gerenciando o LED e o buzzer com base na leitura do sensor. O projeto visa verificar se um objeto foi corretamente agarrado pelo braço robótico, oferecendo feedback visual, auditivo e textual sobre a detecção de objetos.

Adicionalmente, é descrita uma API de Gerenciamento de Kits, que disponibiliza uma série de endpoints para a manipulação de kits, posições de kits, registro de usuários e itens, e consultas relacionadas. Os endpoints oferecem funcionalidades como a consulta de kits, adição de novos kits, registro de usuários, autenticação de login, criação de posições de kit, registro de itens, consulta de posições de kit, consulta de itens, criação de pedidos de kit, consulta de pedidos de kit, atualização de status de pedidos de kit e consulta de pedidos de kit por status. Cada endpoint é detalhadamente descrito quanto à sua função, parâmetros de requisição e resposta, e código de status HTTP correspondente. O texto ressalta a organização e a eficiência da API para o gerenciamento abrangente de dados relacionados a kits.


## Log de tarefas
<div className = "borda_imagens">
    ![Log de tarefas Sprint 3](/img/log-tarefas-sprint3.png)
</div>
<h6 align="center"> Fonte: Elaboração Grupo 4U </h6>