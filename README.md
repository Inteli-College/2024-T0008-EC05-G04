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

## Estrutura do Projeto

O projeto está estruturado de acordo com as seguintes pastas:

- `src/`: Contém o código-fonte do projeto.
  - `firmware/`: O código-fonte para a Raspberry Pi Pico W
  - `robot/`: O código-fonte para a comunicação com o Dobot
  - `backend/`: Código-fonte para o backend do projeto
  - `frontend/`: Código-fonte para o frontend do projeto
- `docs/`: Documentação do projeto feita no Docussaurus.

## Execução do Projeto

A execução depende da parte do projeto que deve ser executada, mas um passo importante antes de qualquer uma é clonar o projeto

```sh
git clone https://github.com/Inteli-College/2024-T0008-EC05-G04.git
```

### Documentação

A documentação é feita com o [Docussaurus], para executá-la, basta executar os seguintes comandos:

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
uvicorn main:app --reload
```

Além disso, é necessária a criação de um arquivo `tokens.py` com o seguinte conteúdo

```py
DATABASE_URL = ''
```

A variável deve representar o ponto de acesso ao seu banco de dados

## Objetivo do Projeto

## Equipe de Desenvolvimento

| ![Cecília Gonçalves](https://media.licdn.com/dms/image/D4E03AQHFDADl2nqTcA/profile-displayphoto-shrink_400_400/0/1680660675815?e=1715817600&v=beta&t=BFo5ZLvGmbYiAuvyB4BM-VPZ-AZNbZuFUXstYD2TbEo) | ![Eduardo Barreto](https://media.licdn.com/dms/image/D4D03AQHcmdXszbRiEA/profile-displayphoto-shrink_400_400/0/1674764017034?e=1715817600&v=beta&t=yEZlT7csCzV9X5hPPXbEMFqodOQdWPqENCtDb4j9KXQ) | ![Fernando Vasconcelos](https://media.licdn.com/dms/image/D4D03AQG_T8Nvtk_lNg/profile-displayphoto-shrink_400_400/0/1677155884081?e=1715817600&v=beta&t=jeDWU5tQBxQTaGhNIdBPU6Bggcj_Tft4LcbllaIcN4c) | ![Lidia Mariano](https://media.licdn.com/dms/image/D4D03AQG56mwRJ4G55g/profile-displayphoto-shrink_400_400/0/1675023865459?e=1715817600&v=beta&t=A8-s9zf8_CMeBnfyaOvnKUlDTuGIjnsBKYFkEa2FE84) | ![Luan Ramos](https://media.licdn.com/dms/image/D4D03AQF5k4FEfaI4mg/profile-displayphoto-shrink_400_400/0/1698150342373?e=1715817600&v=beta&t=B498NfoBN5UtE0gVYnZ6a9CMnkhLvvvjaugz0V2n2us) | ![Murilo Prianti](https://media.licdn.com/dms/image/D4D35AQG6W_7TsJCfoQ/profile-framedphoto-shrink_400_400/0/1655926445979?e=1711051200&v=beta&t=DtVZslhMKVngcGdEoaossz4GnvXq8cZiQDrwi2mGIgY) | ![Ólin Costa](https://media.licdn.com/dms/image/D4D03AQHMcFlvJWMv_Q/profile-displayphoto-shrink_400_400/0/1707441102331?e=1715817600&v=beta&t=BrXbtUAef7Uf0tw-Q4n2QY8lAeyA6r1sKx0hanrs0KA) |
| :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|                                                  [Cecília Gonçalves](https://www.linkedin.com/in/cec%C3%ADlia-alonso-gon%C3%A7alves-3aa4bb271/)                                                   |                                                                 [Eduardo Barreto](https://www.linkedin.com/in/eduardosbarreto/)                                                                 |                                                      [Fernando Vasconcelos](https://www.linkedin.com/in/fernando-antonio-s-c-de-vasconcellos/)                                                       | [Lidia Mariano](https://www.linkedin.com/in/lidiamariano/)                                                                                                                                    | [Luan Ramos](https://www.linkedin.com/in/luan-ramos-de-mello-253b28268/)                                                                                                                   | [Murilo Prianti](https://www.linkedin.com/in/murilo-prianti-0073111a1/)                                                                                                                       | [Ólin Costa](https://www.linkedin.com/in/%C3%B3lin-medeiros-costa-b0a1b426a/)                                                                                                              |

## Licença

Este projeto está licenciado sob a Licença CC-0. Veja o arquivo `LICENSE` para mais detalhes.

## Documentação

A documentação do projeto está disponível no [Github Pages](https://inteli-college.github.io/2024-T0008-EC05-G04/).
