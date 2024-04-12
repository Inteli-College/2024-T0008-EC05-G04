# Requisitos funcionais

Para a elaboração de uma arquitetura de solução consistente, é necessário que os requisitos funcionais sejam bem delimitados e suficientes haja vista que eles determinam a forma que a solução deve tomar. Objetivamente, os requisitos funcionais "é um requisito que se refere a um resultado de comportamento que deve ser provido por uma funcionalidade do sistema"[1]. Dessa forma, os requisitos funcionais buscam explicar quais são as capacidades do sistema, sendo assim, considerados a base do projeto, visto que guiam as funcionalidades que a plataforma terá. Em suma, os requisitos funcionais especificam o que o sistema deve fazer — suas funções, operações e comportamentos esperados. Portanto, delimitamos abaixo os requisitos funcionais do projeto desenvolvido.
 

| Requisitos Funcionais | Descrição  |
| --- | --- |
| RF01 | O sistema deve possuir um banco de dados para armazenar os kits. |
| RF02 | A aplicação web deve permitir salvar novos layouts de kits. |
| RF03 | A aplicação web deve ter uma funcionalidade de edição de layout. |
| RF04 | A aplicação web deve registrar os itens utilizados na montagem de um determinado kit. |
| RF05 | O sistema deve ser capaz de montar o kit selecionado pelo usuário. |
| RF06 | O sistema deve ser capaz de interagir com diferentes itens para a montagem do kit. |

### RF01 - O sistema deve possuir um banco de dados para armazenar os kits. 
Deve haver um banco de dados, capaz de armazenar os layouts dos kits, permitindo gravar tanto a posição do item no layout de entrada, quanto no layout de saída. Além disso, é necessário permite gravar quais são os itens, integrando com o sistema utilizado para controle atualmente. 

### RF02 - A aplicação web deve permitir salvar novos layouts de kits.
A aplicação web deve possuir uma funcionalidade permitindo inserir novos registros de kits no banco de dados. Assim, possibilitando a criação de um novo kit ainda não cadastro no software ser montado pelo braço mecânico.

### RF03 -  A aplicação web deve ter uma funcionalidade de edição de layout. 
O site deve permitir a alteração de um layout, caso haja a necessidade de modificar um layout de kit já existente ou seus itens. Ademais, o layout deve ser salvo no banco de dados, para permitir que seja carregado no robô.

### RF04 - A aplicação web deve registrar os itens utilizados na montagem de um determinado kit.
A aplicação web tem que ser capaz de permitir o usuário selecionar todos os itens utilizados em um kit, assim como salvar essas informações no banco de dados.

### RF05 - O sistema deve ser capaz de montar o kit selecionado pelo usuário.
O braço robótico deve ser capaz de realizar a montagem do kit.

### RF06 - O sistema deve ser capaz de interagir com diferentes itens para a montagem do kit.
O braço robótico deve ser capaz de interagir com vários tipos de objetos, devido a diversidade de itens presentes nos diferentes kits.

## Referências
[1] ENGENHARIA de Requisitos. [S. l.]: Soluções Educacionais Integradas, [2020]. Disponível em: https://integrada.minhabiblioteca.com.br/reader/books/9786556900674/pageid/34. Acesso em: 15 fev. 2024.

