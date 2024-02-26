# CLI - Interface de Linha de Comando

Um CLI ou Command Line Interface é, como o nome sugere, uma interface que permite aos usuários interagirem com um programa através de uma linha de comando.

Este CLI fornece comandos para controlar um robô usando o módulo DobotController. Abaixo estão os comandos disponíveis juntamente com suas descrições e uso.

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
[![Comando Move](https://www.youtube.com/watch?v=dQw4w9WgXcQ)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

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
[![Comando Move To](https://www.youtube.com/watch?v=dQw4w9WgXcQ)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

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
[![Comando Home](https://www.youtube.com/watch?v=dQw4w9WgXcQ)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

---

## 4. Comando Enable Tool

### Descrição
Ativa a ferramenta do robô.

### Uso
```bash
$ python src/main.py enable_tool [--time-to-wait]
```

- `--time-to-wait` (Opcional): Tempo de espera para ativar a ferramenta (o padrão é 200).

### Demonstração em Vídeo
[![Comando Enable Tool](https://www.youtube.com/watch?v=dQw4w9WgXcQ)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

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
[![Comando Disable Tool](https://www.youtube.com/watch?v=dQw4w9WgXcQ)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

---

## 6. Comando Current

### Descrição
Exibe a posição atual do robô.

### Uso
```bash
$ python src/main.py current
```

### Demonstração em Vídeo
[![Comando Current](https://www.youtube.com/watch?v=dQw4w9WgXcQ)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

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
[![Comando Save](https://www.youtube.com/watch?v=dQw4w9WgXcQ)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

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
[![Comando Run](https://www.youtube.com/watch?v=dQw4w9WgXcQ)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

---

## 9. Comando Control

### Descrição
Abre a interface de controle para seleção interativa de comandos.

### Uso
```bash
$ python src/main.py control
```

### Demonstração em Vídeo
[![Comando Control](https://www.youtube.com/watch?v=dQw4w9WgXcQ)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

---
