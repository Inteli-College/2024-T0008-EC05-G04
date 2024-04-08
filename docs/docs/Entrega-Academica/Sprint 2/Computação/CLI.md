# CLI - Interface de Linha de Comando

Um CLI ou Command Line Interface é, como o nome sugere, uma interface que permite aos usuários interagirem com um programa através de uma linha de comando.

Este CLI fornece comandos para controlar um robô usando o módulo DobotController. Abaixo estão os comandos disponíveis juntamente com suas descrições e uso.

# Estrutura de pastas e arquivos

- `dobotController.py`: Responsável por ser uma camada de abstração entre o alto nível do código e a movimentação do robô. Os outros arquivos chamam ele para executar as tarefas.
- `mock_pydobot.py`: Responsável por _mockar_ o comportamento do robô, facilitando os testes e melhorias quando não temos acesso ao robô. Ele funciona imprimindo a saída no console, simulando os posicionamentos.
- `position.py`: Responsável por definir a classe que representa uma posição, ajudando na transferência de dados entre os programas e facilitando operações matemáticas.
- `positions.json`: Responsável pela calibração do robô, ele é quem dita quais são as posições dos slots dos kits.

# Comandos

## 1. Comando Move

### Descrição

Move o robô por uma distância específica ao longo de um eixo especificado.

### Uso

```bash
$ python src/main.py move <eixo> <distância> [--wait]
```

- `<eixo>`: Eixo a ser movido (por exemplo, X, Y, Z, R).
- `<distância>`: Distância a ser percorrida no eixo especificado.
- `--wait` (Opcional): Aguarde o movimento ser concluído (o padrão é True).

### Demonstração em Vídeo

<iframe width="560" height="315" src="https://www.youtube.com/embed/hKD8Ji19PuA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---

## 2. Comando Move To

### Descrição

Move o robô para uma posição específica definida por coordenadas X, Y, Z e R.

### Uso

```bash
$ python src/main.py move_to <x> <y> <z> <r> [--wait]
```

- `<x>`: Coordenada X para mover.
- `<y>`: Coordenada Y para mover.
- `<z>`: Coordenada Z para mover.
- `<r>`: Coordenada R para mover.
- `--wait` (Opcional): Aguarde o movimento ser concluído (o padrão é True).

### Demonstração em Vídeo

<iframe width="560" height="315" src="https://www.youtube.com/embed/hKD8Ji19PuA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---

## 3. Comando Home

### Descrição

Move o robô para a posição inicial (home).

### Uso

```bash
$ python src/main.py home [--wait]
```

- `--wait` (Opcional): Aguarde o robô atingir a posição inicial (o padrão é True).

### Demonstração em Vídeo

## <iframe width="560" height="315" src="https://www.youtube.com/embed/ALBMLxbuuSc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## 4. Comando Enable Tool

### Descrição

Ativa a ferramenta do robô.

### Uso

```bash
$ python src/main.py enable_tool [--time-to-wait]
```

- `--time-to-wait` (Opcional): Tempo de espera para ativar a ferramenta (o padrão é 200).

### Demonstração em Vídeo

<iframe width="560" height="315" src="https://www.youtube.com/embed/D-s1rjEve8Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---

## 5. Comando Disable Tool

### Descrição

Desativa a ferramenta do robô.

### Uso

```bash
$ python src/main.py disable_tool [--time-to-wait]
```

- `--time-to-wait` (Opcional): Tempo de espera para desativar a ferramenta (o padrão é 200).

### Demonstração em Vídeo

<iframe width="560" height="315" src="https://www.youtube.com/embed/lIgo7XGcVLI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---

## 6. Comando Current

### Descrição

Exibe a posição atual do robô.

### Uso

```bash
$ python src/main.py current
```

### Demonstração em Vídeo

<iframe width="560" height="315" src="https://www.youtube.com/embed/Kxa3wUqeWWI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---

## 7. Comando Save

### Descrição

Salva a posição atual do robô em um arquivo.

### Uso

```bash
$ python src/main.py save <caminho-do-arquivo>
```

- `<caminho-do-arquivo>`: Caminho para salvar a posição atual.

### Demonstração em Vídeo

<iframe width="560" height="315" src="https://www.youtube.com/embed/zZCVIMzcc-Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---

## 8. Comando Run

### Descrição

Executa uma lista de posições de um arquivo.

### Uso

```bash
$ python src/main.py run <caminho-do-arquivo>
```

- `<caminho-do-arquivo>`: Caminho para o arquivo com as posições.

### Demonstração em Vídeo

<iframe width="560" height="315" src="https://www.youtube.com/embed/zZCVIMzcc-Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---

## 9. Comando Control

### Descrição

Abre a interface de controle para seleção interativa de comandos.

### Uso

```bash
$ python src/main.py control
```

### Demonstração em Vídeo

<iframe width="560" height="315" src="https://www.youtube.com/embed/Es02nD8bEMk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---
