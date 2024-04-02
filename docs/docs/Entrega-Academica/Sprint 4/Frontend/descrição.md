# Descrição do Frontend

## Introdução 
O frontend do projeto foi desenvolvido para oferecer uma interface intuitiva e dinâmica na configuração e operação do braço robótico de montagem de kits de emergência. Através desta interface, os responsáveis podem configurar o robô, selecionar ou criar layouts dos kits, e acessar estatísticas detalhadas sobre a utilização dos medicamentos e a eficiência das montagens.

O objetivo principal é melhorar a experiência do usuário com o sistema. A seleção e criação de layouts para carrinhos de emergência possibilita aos usuários a opção de escolher entre as opções pré-definidas ou personalizar novos layouts de acordo com suas demandas. Além disso, é disponibilizado um painel de informações com informações sobre a saída de medicamentos e o desempenho das montagens. Essa funcionalidade proporciona uma análise mais aprofundada e um acompanhamento eficaz do desempenho operacional.

Esses elementos visam não apenas aprimorar a eficiência e a personalização do sistema, mas também fornecer informações valiosas para a tomada de decisões e a melhoria contínua dos processos.

## Tecnologias Utilizadas

**React JS**

O React JS é uma biblioteca front-end JavaScript com foco em criar interfaces de usuário em páginas web. Foi utilizado como base do frontend do projeto, proporcionando uma experiência de usuário fluida. Ao dividir a aplicação em páginas e componentes reutilizáveis, como a NavBar, a equipe maximizou a modularidade e a eficiência do desenvolvimento. O React permitiu a criação de uma interface interativa que facilita a configuração do robô, a seleção e criação de layouts de carrinhos de emergência, além de visualizar estatísticas através de um dashboard. A escolha do React JS se destacou por ser uma linguagem que os membros do grupo já conheciam, por otimizar o desempenho, acelerar o desenvolvimento e oferecer flexibilidade para expansões futuras, atendendo às necessidades do projeto.

**TypeScript**

A escolha do TypeScript para o projeto foi motivada pelo seu caráter de linguagem tipada, que fornece relatórios de erros em tempo real durante o desenvolvimento. Essa característica fundamental do TypeScript permitiu que a equipe identificasse e resolvesse problemas de forma proativa, antes mesmo da fase de criação ou execução. A habilidade de identificar erros e discrepâncias em código de forma imediata, em um ambiente de desenvolvimento, não apenas agilizou o processo de criação, mas também aprimorou significativamente a qualidade do código final.

**Tailwind CSS**

O Tailwind CSS teve um papel relevante no projeto, fornecendo uma abordagem eficiente para a estilização do frontend. Por meio deste framework, foi possível aplicar estilos diretamente no TSX das páginas React, o que aprimorou o processo de criação e propiciou ajustes de design ágeis. Com o Tailwind, a equipe personalizou a paleta de cores, a disposição dos elementos e criou interações por meio de estados como o hover. Essa abordagem resultou em uma interface visualmente agradável, o que impacta significativamente a experiência do usuário sem complicar o código, garantindo uma aplicação esteticamente e funcionalmente rica.

**Mui**

O Mui é uma biblioteca de componentes de interface do usuário (UI) desenvolvida para facilitar a criação de aplicativos web modernos e responsivos. Essa ferramenta otimizou o tempo de desenvolvimento da equipe, aproveitando seus componentes UI prontos para uso e adaptáveis. Dentro do frontend do projeto, o Mui foi utilizado para criar os componentes dropdown e autocomplete, por exemplo.

**Chart.js**

O Chart.js é uma biblioteca JavaScript gratuita para visualização de dados, oferecendo diversos tipos de gráficos. Essa ferramenta foi integrada para gerar gráficos dinâmicos no dashboard, facilitando o entendimento das informações. Por exemplo, foram implementados gráficos de barras para visualizar em que intervalo de tempo o kit foi mais utilizado, gráficos de pizza para representar a quantidade de kits por layout e gráficos de linha para mostrar a ocorrência de cada kit.

**Faker.js**

O Faker.js é uma biblioteca que torna mais simples a criação de dados fictícios para testes, sem a necessidade de criar dados manualmente, permitindo que a equipe se concentre apenas no desenvolvimento das telas. A criação de informações fictícias de kits, layouts e medicamnetos foi empregada pela equipe para validar o dashboard e gerar gráficos com essas informações, uma vez que ainda não existem informações reais.

## Conclusão
Este frontend foi desenvolvido para atuar como uma ferramenta eficaz e de fácil uso para os responsáveis pela operação do sistema de montagem de kits de emergência do Hospital Sírio-Libanês. Ele permite a escolha e personalização de layouts de kits, além de prover acesso a informações cruciais sobre o processo através de estatísticas detalhadas. Cada tecnologia incorporada neste projeto foi selecionada e implementada visando maximizar a facilidade de uso, a eficiência no desenvolvimento e a facilidade de manutenção do sistema, garantindo assim uma solução adaptável às necessidades dos operadores.

