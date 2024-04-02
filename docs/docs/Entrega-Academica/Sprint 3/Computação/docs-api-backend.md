# Documentação da API de Gerenciamento de Kits

Esta API fornece um conjunto de endpoints para gerenciar kits, posições de kits, registro de usuários e itens, e consultas relacionadas.

## Endpoints

### Consultar Todos os Kits

- **GET** `/kits`
  - **Descrição**: Retorna todos os kits disponíveis.
  - **Resposta**: `200 OK`
    ```json
    [
      {
        "id": 0,
        "name": "string",
        "quantity": 0
      }
    ]
    ```

### Adicionar um Novo Kit

- **POST** `/add-kit`
  - **Descrição**: Adiciona um novo kit ao sistema.
  - **Corpo da Requisição**:
    ```json
    {
      "name": "string",
      "quantity": 0
    }
    ```
  - **Resposta**: `201 Created`

### Registrar Usuário

- **POST** `/register`
  - **Descrição**: Registra um novo usuário no sistema.
  - **Corpo da Requisição**:
    ```json
    {
      "user": "string",
      "password": "string"
    }
    ```
  - **Resposta**: `201 Created`

### Login

- **POST** `/login`
  - **Descrição**: Autentica um usuário no sistema.
  - **Corpo da Requisição**:
    ```json
    {
      "user": "string",
      "password": "string"
    }
    ```
  - **Resposta**:
    - `200 OK` para usuário autorizado.
    - `Unauthorized` para usuário não autorizado.

### Criar Posição de Kit

- **POST** `/kitPositionCreate`
  - **Descrição**: Adiciona uma nova posição de kit.
  - **Corpo da Requisição**:
    ```json
    {
      "kit_id": 0,
      "position": 0,
      "item_id": 0
    }
    ```
  - **Resposta**: `201 Created`

### Registrar Item

- **POST** `/item-register`
  - **Descrição**: Registra um novo item no sistema.
  - **Corpo da Requisição**:
    ```json
    {
      "name": "string",
      "expire": "2024-03-14",
      "manufacturer": "string",
      "batch": "string"
    }
    ```
  - **Resposta**: `201 Created`

### Consultar Posições de Kit

- **GET** `/kit-position/{kit_id}`
  - **Descrição**: Retorna todas as posições de um kit específico.
  - **Resposta**: `200 OK`
    ```json
    [
      {
        "id": 0,
        "kit_id": 0,
        "position": 0,
        "item_id": 0
      }
    ]
    ```

### Consultar Itens

- **GET** `/itens`
  - **Descrição**: Retorna todos os itens ou itens filtrados por ID.
  - **Parâmetros Opcionais**:
    - `item_id` (query): Filtra itens por ID.
  - **Resposta**: `200 OK`
    ```json
    [
      {
        "id": 0,
        "name": "string",
        "expire": "2024-03-14",
        "manufacturer": "string",
        "batch": "string"
      }
    ]
    ```

### Criar Pedido de Kit

- **POST** `/kit-order`
  - **Descrição**: Cria um novo pedido de kit.
  - **Corpo da Requisição**:
    ```json
    {
      "kit_id": 1,
      "requested_by": 0
    }
    ```
  - **Resposta**: `201 Created`

### Consultar Pedidos de Kit

- **GET** `/kit-orders`
  - **Descrição**: Retorna todos os pedidos de kit ou filtrados por `requested_by`.
  - **Resposta**: `200 OK`

### Atualizar Status do Pedido de Kit

- **PATCH** `/kit-order/{order-id}/status`
  - **Descrição**: Atualiza o status de um pedido de kit específico e incrementa o campo quantity na coluna kits.
  - **Corpo da Requisição**:
    ```json
    {
      "new_status": "executed"
    }
    ```
  - **Resposta**: `200 OK`

### Consultar Pedidos de Kit por Status

- **GET** `/execute`

  - **Descrição**: Retorna todos os pedidos de kit filtrados por status.

  - **Parâmetros Opcionais**:
    - `status` (query): Filtra pedidos por status.
  - **Resposta**: `200 OK`

---

Cada endpoint é projetado para uma função específica dentro do sistema de gerenciamento de kits, permitindo a criação, atualização, e consulta de dados de forma eficiente e organizada.
