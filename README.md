<!-- Critérios -->
<!-- - [Crítico] Apresenta a estrutura do projeto (como as demais pastas estão organizadas)? -->
<!-- - [Crítico] Apresenta instruções claras de como executar o projeto e a documentação? -->
<!-- - Apresenta o objetivo do projeto? -->
<!-- - Apresenta os integrantes da equipe de desenvolvimento? -->
<!-- - Apresenta o link do Linkdin ou Github dos integrantes da equipe? -->
<!-- - Apresenta a licença Inteli do projeto (CC-0)? -->
<!-- - Apresenta os dados dos integrantes da equipe, o nome da equipe e o nome do Inteli na seção de licensa do projeto? -->
<!-- - Possui um link para o Github Pages onde a documentação pode ser localizada? -->

<p align="center">
    <img src="docs/static/img/logo/png/logo-no-background.png" alt="4U"/>
</p>
<h1 align="center">4U</h1>
<p align="center"><b>Inteli 2024-T0008-EC05-G04.</b></p>

## Descrição do Projeto

Devido à constante procura e necessidade de agilizar processos no setor de saúde, o Hospital Sírio-Libanês identificou a chance de aprimorar a montagem dos kits hospitalares de emergência. O grupo 4U, em parceria com o Alma Sírio-Libanês, vertente de tecnologia do hospital, desenvolveu um projeto de um sistema de automação, para que esse processo se torne mais eficiente.


## Objetivo do Projeto

Esse projeto não apenas tem como objetivo acelerar a montagem dos kits, mas também assegurar a a segurança necessária para atender as diversas demandas emergenciais. Ao aliviar a equipe de saúde das tarefas operacionais, o sistema permite que estes profissionais se concentrem no que realmente importa: prestar um atendimento rápido e cuidadoso aos pacientes. A expectativa é que essa inovação não só eleve o padrão dos serviços oferecidos, mas também otimize a utilização dos recursos, minimize os tempos de resposta em situações críticas e reforce a segurança dos pacientes. 

Tais objetivos são atingidos por meio da implementação de um braço robótico acompanhado de uma interface gráfica de operação, a qual permite que kits sejam cadastrados e o processo de operação do robô para montagem do kit possa ser realizado com pouquíssimo treinamento.

## Estrutura do Projeto

O projeto está estruturado de acordo com as seguintes pastas:

```
├── docs
│   ├── docs
│   │   └── Entrega-Academica
│   │       ├── Sprint 1
│   │       │   ├── Arquitetura
│   │       │   ├── Negocios
│   │       │   └── UX
│   │       ├── Sprint 2
│   │       │   ├── Computação
│   │       │   └── UX
│   │       ├── Sprint 3
│   │       │   └── Computação
│   │       ├── Sprint 4
│   │       │   └── Frontend
│   │       └── Sprint 5
│   ├── src
│   │   ├── components
│   │   │   └── HomepageFeatures
│   │   └── css
│   └── static
│       ├── img
│       │   ├── apresentacao1
│       │   ├── apresentacao2
│       │   └── logo
│       │       ├── pdf
│       │       ├── png
│       │       └── svg
│       └── sheets
└── src
    ├── backend
    │   └── src
    │       ├── controllers
    │       │   ├── itens
    │       │   ├── kit_orders
    │       │   ├── kit_positions
    │       │   ├── kits
    │       │   └── robots
    │       ├── models
    │       ├── routers
    │       └── schemas
    ├── firmware
    │   └── src
    ├── frontend
    │   ├── public
    │   └── src
    │       ├── components
    │       ├── hooks
    │       ├── interfaces
    │       ├── pages
    │       └── static
    └── robot
        └── src
```

## Execução do Projeto

A execução depende da parte do projeto que deve ser executada, mas um passo importante antes de qualquer uma é clonar o projeto

```sh
git clone https://github.com/Inteli-College/2024-T0008-EC05-G04.git
```

### Documentação

A documentação é feita com o [Docussaurus](https://docusaurus.io/), para executá-la, basta executar os seguintes comandos:

```sh
cd docs
npm i
npm start
```

### Robot

Após a instalação do [python3](https://www.python.org/), para executar o código do robô, execute os comandos abaixo

```
cd src/robot
pip install -r requirements.txt
python3 src/app.py
```

### Firmware

Para a execução do firmware, é necessária a instalação do software Thonny e a gravação da Raspberry Pi Pico W através de sua interface.

Além disso, é necessária a criação de um arquivo `tokens.py` com o seguinte conteúdo

```py
SSID = ''
PASSWORD = ''
BASE_URL = ''
```

nas variáveis é preciso colocar as informações da sua rede

### Backend

Após a instalação do [python3](https://www.python.org/), para executar o backend, execute os comandos abaixo

```
cd src/backend
pip install -r requirements.txt
python3 src/main.py
```

Além disso, é necessária a criação de um arquivo `tokens.py` com o seguinte conteúdo

```py
DATABASE_URL = ''

ROBOT_URL = '' 
```

nas variáveis é preciso colocar as informações de acesso do seu backend e a url que o robô está rodando.

### Frontend

Para rodar o frontend, execute os comandos abaixo

```sh
cd src/frontend/my-app
npm i
npm start
```

## Equipe de Desenvolvimento

| ![Cecília Gonçalves](https://media.licdn.com/dms/image/D4E03AQHFDADl2nqTcA/profile-displayphoto-shrink_400_400/0/1680660675815?e=1723075200&v=beta&t=utZUw_RsEFBLnNEHQHYwJaJzeiuCi5fcta_zU591eaQ) | ![Eduardo Barreto](https://media.licdn.com/dms/image/D4D03AQHcmdXszbRiEA/profile-displayphoto-shrink_400_400/0/1674764017034?e=1723075200&v=beta&t=hkt4Nns4Z-b6XMKWoKPSs0bnAHAeyo3XHXnJtb0j_L8) | ![Fernando Vasconcelos](https://media.licdn.com/dms/image/D4D03AQG_T8Nvtk_lNg/profile-displayphoto-shrink_400_400/0/1677155884081?e=1723075200&v=beta&t=eXhHTAGsOiIkql3YvgQqsNHG_QJMnDvvwgffSumxSLY) | ![Lidia Mariano](https://media.licdn.com/dms/image/D4D03AQG56mwRJ4G55g/profile-displayphoto-shrink_400_400/0/1675023865459?e=1723075200&v=beta&t=eI9JX-n0cGLK-kvGUN3SBKAf-w8aTj0RRxo_EzaL5ic) | ![Luan Ramos](https://media.licdn.com/dms/image/D4D03AQF5k4FEfaI4mg/profile-displayphoto-shrink_400_400/0/1698150342373?e=1715817600&v=beta&t=B498NfoBN5UtE0gVYnZ6a9CMnkhLvvvjaugz0V2n2us) | ![Murilo Prianti](https://media.licdn.com/dms/image/D4D35AQGP2ySXkAn_wA/profile-framedphoto-shrink_400_400/0/1715367450460?e=1718218800&v=beta&t=_9GYprjCy3vJsSmIUgWaV9O6O5KixSlf1O9CwZqDgGI) | ![Ólin Costa](https://media.licdn.com/dms/image/D4D03AQHMcFlvJWMv_Q/profile-displayphoto-shrink_400_400/0/1707441102331?e=1723075200&v=beta&t=Rmd99KC5tIrGSnY8YhNXe8d0srXk3qHkFtZ5rheKSxk) |
| :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|                                                  [Cecília Gonçalves](https://www.linkedin.com/in/cec%C3%ADlia-alonso-gon%C3%A7alves-3aa4bb271/)                                                   |                                                                 [Eduardo Barreto](https://www.linkedin.com/in/eduardosbarreto/)                                                                 |                                                      [Fernando Vasconcelos](https://www.linkedin.com/in/fernando-antonio-s-c-de-vasconcellos/)                                                       | [Lidia Mariano](https://www.linkedin.com/in/lidiamariano/)                                                                                                                                    | [Luan Ramos](https://www.linkedin.com/in/luan-ramos-de-mello-253b28268/)                                                                                                                   | [Murilo Prianti](https://www.linkedin.com/in/murilo-prianti-0073111a1/)                                                                                                                       | [Ólin Costa](https://www.linkedin.com/in/%C3%B3lin-medeiros-costa-b0a1b426a/)                                                                                                              |

## Licença

4U by Inteli - Cecília Gonçalves, Eduardo Barreto, Fernando Vasconcelos, Lidia Mariano, Luan Ramos, Murilo Prianti, Ólin Costa is licensed under CC BY 4.0 

---

A documentação completa pode ser encontrada em https://inteli-college.github.io/2024-T0008-EC05-G04/
