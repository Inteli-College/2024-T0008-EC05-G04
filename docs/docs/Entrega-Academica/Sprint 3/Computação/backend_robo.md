# Controle do robô através do BackEnd

Para conseguir controlar o robô através de uma aplicação web, além de um BackEnd que interage com o banco de dados, foi desenvolvido uma aplicação em python. Para realizar a tarefa, ela se conecta com o robô via cli, porém após isso inicia uma aplicação flask, permitindo receber requisições e enviando instruções ao robô.

## EndPoint Primário - /kit-order

Esse endpoint permite a execução de um determinado kit. Com isso, é necessário enviar um parâmetro, no json, contendo um objeto do tipo `kit order`. Nesse objeto, terá uma lista de objetos do tipo `kit`, sendo que cada `kit` tem um nome e posição. Assim, permitindo ao app.py iterar sobre ele.
Para realizar a movimentação de cada item, é necessário realizar uma conversão da posição em coordenadas, através do arquivo `position.json`. Após isso, é invocada a função `move_item`, recebendo esse dicionário de coordenadas e movendo o robô para cada uma de suas respectivas posições.  

## EndPoint Raspberry 

Além do endpoint principal, há um endpoint secundário, no qual a raspberry se comunica com o robô, fornecendo informações se o item foi pego ou não. Para isso, é enviado uma variável na requisição que contém a distância do item até o sensor, e feita a verificação no código. Essa informação é utilizada na hora de montar um kit, e faz com que seja executado 3 vezes a tentativa de pegar um item caso ele não consiga de primeira.