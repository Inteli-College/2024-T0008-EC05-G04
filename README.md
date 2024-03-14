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
python3 src/main.py
```

## Objetivo do Projeto

## Equipe de Desenvolvimento

| ![Cecília Gonçalves](link_da_foto) | ![Eduardo Barreto](link_da_foto) | ![Fernando Vasconcelos](link_da_foto) | ![Lidia Mariano](link_da_foto) | ![Luan Ramos](link_da_foto) | ![Murilo Prianti](link_da_foto) | ![Ólin Costa](link_da_foto) |
| :--------------------------------: | :------------------------------: | :-----------------------------------: | ------------------------------ | --------------------------- | ------------------------------- | --------------------------- |
| [Cecília Gonçalves](linkedin)  | [Eduardo Barreto](linkedin)  | [Fernando Vasconcelos](linkedin)  | [Lidia Mariano](linkedin)  | [Luan Ramos](linkedin)  | [Murilo Prianti](linkedin)  | [Ólin Costa](linkedin)  |

## Licença

Este projeto está licenciado sob a Licença CC-0. Veja o arquivo `LICENSE` para mais detalhes.

## Documentação

A documentação do projeto está disponível no [Github Pages](https://inteli-college.github.io/2024-T0008-EC05-G04/).
