# Fluxo de Utilização da Solução


;O Fluxo de Utilização da Solução delineia como os usuários interagem com a solução, nesse caso com a automação. Esse fluxo é crucial para que a compreensão de como a solução será aplicada seja garantida, detalhando as etapas específicas que cada usuário deve seguir. Ao fornecer o diagrama de fluxo, juntamente com uma descrição, pode-se assegurar o entendimento sobre a experiência do usuário e que a solução atenda às necessidades dos usuários. 


## Fluxo da Gestora Hospitalar

;Esse fluxo é referente à persona da Gestora Hospitalar, ele destina-se a ilustrar o processo desde a chegada no posto de trabalho e sua utilização no software.

![Fluxo Gestora Hospitalar](/img/fluxo-mayumi.png)

<p align="center"><b>Figura 1 - </b> Fluxo Gestora Hospitalar</p>
<p align="center">Fonte: Elaboração Grupo 4</p>

## Wireframe da Gestora Hospitalar

;A interação entre a gestora hospitalar e a solução é fundamental para garantir não apenas a segurança dos kits montados, mas também para explorar os dados armazenados pela plataforma, visando a geração de insights que otimizem a administração hospitalar. O wireframe da Mayumi apresenta uma tela inicial, oferecendo funcionalidades essenciais para a gestão eficaz. Dentre essas funcionalidades, destacam-se a visualização de kits, a criação de novos kits e o acesso às estatísticas.

;A Mayumi começa fazendo o login no software, segue para um menu de funcionalidades no qual ela pode escolher o que deseja ver aquele momento no site. Após a escolha ser feita ela será redirecionada para a tela incial.

### Tela 1 - Login

![Tela de Login](/img/wireframe-login.png)

<p align="center"><b>Figura 2 - </b> Tela de Login</p>
<p align="center">Fonte: Elaboração Grupo 4</p>

### Tela 2 - Recuperação

![Tela de Login 2](/img/wireframe-login-email.png)

<p align="center"><b>Figura 3 - </b> Tela de Login Email e Senha</p>
<p align="center">Fonte: Elaboração Grupo 4</p>

;Ao acessar a tela inicial, a gestora depara-se com três opções principais, cada uma abrindo caminho para diferentes aspectos da gestão de kits e dados. O primeiro card conduz à tela de visualização de kits, onde a gestora pode examinar detalhadamente os componentes de cada kit disponível. Essa jornada específica será melhor explorada em na explicação da jornada da persona do auxiliar de farmácia, uma vez que se alinha de forma mais precisa com as necessidades e fluxo de trabalho da persona Gabriel Menino.

### Tela 3 - Inicial de funcionalidades

![Tela inicial de funcionalidades](/img/wireframe-funcionalidade.png)

<p align="center"><b>Figura 4 - </b> Tela inicial de funcionalidades</p>
<p align="center">Fonte: Elaboração Grupo 4</p>

; O segundo card direciona à tela de criação e edição de kits, fornecendo à gestora uma interface intuitiva para compor novos conjuntos de materiais. Neste processo, ela é guiada a selecionar a posição de cada item no carrinho e a preencher os campos necessários, como o nome do kit, os itens a serem incluídos e as quantidades desejadas. Todos os campos são automaticamente preenchidos, simplificando a tarefa. Após a conclusão, ao clicar no botão "Salvar", um pop-up confirma a criação do kit, garantindo um feedback claro e imediato sobre a ação realizada.

### Tela 4 - Criar/editar kit

![Tela de criar/editar kit](/img/editar-kit.png)

<p align="center"><b>Figura 5 - </b> Tela de criar/editar kit</p>
<p align="center">Fonte: Elaboração Grupo 4</p>

### Pop up da tela de criar/editar kit

![Pop up da tela de criar/editar kit](/img/editar-kit-popup.png)

<p align="center"><b>Figura 5 - </b> Pop up da tela de criar/editar kit </p>
<p align="center">Fonte: Elaboração Grupo 4</p>

; Por fim, o terceiro card conduz à seção de estatísticas, oferecendo à gestora acesso a informações cruciais para a gestão estratégica. Dentro desta seção, há três subseções distintas: tabelas, dashboards e relatórios. Nas tabelas, os kits podem ser visualizados de forma tabular, facilitando a análise detalhada dos componentes e quantidades. Além disso, a opção de exportar os dados para CSV permite uma manipulação mais ampla e personalizada. Os dashboards apresentam os dados das tabelas em formato gráfico, fornecendo uma visualização dinâmica e intuitiva das tendências e padrões. Isso permite à gestora extrair insights valiosos para otimizar a gestão hospitalar. Por fim, os relatórios oferecem uma síntese dos dados mais relevantes em formato PDF, acessíveis através de filtros de datas, tornando-os úteis para apresentações e tomadas de decisão estratégicas. Essa variedade de ferramentas proporciona à gestora hospitalar uma visão abrangente e detalhada de sua operação, capacitando-a a tomar decisões informadas e eficazes.

### Tela 5 - Estatísticas em formato de tabela

![Tela de estatísticas em formato de tabela](/img/estatisticas-tabelas.png)

<p align="center"><b>Figura 6 - </b> Tela de estatísticas em formato de tabela</p>
<p align="center">Fonte: Elaboração Grupo 4</p>

### Tela 6 - Estatísticas em formato de dashboards

![Tela de estatísticas em formato de dashboards](/img/estatisticas-dashboards.png)

<p align="center"><b>Figura 7 - </b> Tela de estatísticas em formato de dashboards</p>
<p align="center">Fonte: Elaboração Grupo 4</p>

### Tela 7 - Estatísticas em formato de relatórios

![Tela de estatísticas em formato de relatórios](/img/estatisticas-relatorios.png)

<p align="center"><b>Figura 8 - </b> Tela de estatísticas em formato de relatórios</p>
<p align="center">Fonte: Elaboração Grupo 4</p>

; O Hospital Sírio Libanês busca automatizar a montagem dos carrinhos de emergência, enfrentando o desafio de layouts variados e modificações frequentes. O objetivo é criar um sistema flexível que permita ajustes e integrações futuras. Com isso, espera-se reduzir o tempo de montagem e gerar relatórios detalhados dos itens utilizados. O projeto envolve a construção de um sistema automatizado capaz de montar diferentes layouts de carrinhos, rastrear os itens e integrar-se com outras soluções. Restrições incluem o uso limitado de uma base robótica em escala reduzida e a não integração com sistemas de login de terceiros.

### Fluxo do auxiliar de farmácia

&emsp; O fluxo a seguir diz respeito a persona do Auxiliar de Farmácia, ele também destina-se a ilustrar o processo desde a chegada no posto de trabalho e sua utilização no software, mostrando que pode ser usado de formas diferentes dependendo de seu objetivo.


### Fluxo Auxiliar de Farmácia

; O fluxo a seguir diz respeito a persona do Auxiliar de Farmácia, ele também destina-se a ilustrar o processo desde a chegada no posto de trabalho e sua utilização no software, mostrando que pode ser usado de formas diferentes dependendo de seu objetivo. 


![Fluxo Auxiliar de Farmácia](/img/fluxo-gabriel.png)

<p align="center"><b>Figura 9 - </b> Fluxo Auxiliar de Farmácia</p>
<p align="center">Fonte: Elaboração Grupo 4</p>

; O Gabriel Menino começa fazendo o login no software, segue para a página de calibração de entrada do robô (alinha a posição do robô em relação ao kit) e depois para página de calibração de saída (alinha a posição conforme os suprimentos), em seguida define os kits e seus itens e verifica se está correto, depois desse passo define quantos kits serão montados baseados na configuração realizada. No próximo momento o braço mecânica realiza a tarefa, após ser completada aparece uma página indicando que o processo de montagem foi finalizado. Se o usuário quiser montar mais um leva de kits, caso queira voltará para página de calibração do robô, se não, ele fecha o programa. Esse fluxo é essencial para entender como uma pessoa dentro do setor da farmácia como responsável direto pelos kits interage com a solução.

## Wireframe - Persona Gabriel Menino

### Tela 1 - Login

; Visando garantir a segurança da plataforma, foi pensado em um sistema de login para evitar usuário externos. Além disso, o sistema de login permite a identificação do usuário, permitindo saber quem realizou cada pedido de kit. Por fim, o sistema permite a distinguição de usuários, garantindo mais funções aos gestores, os quais podem criar e editar um kit, assim como visualizar relatórios sobre os mesmos.

![Wireframe Login](/img/wireframe-login-email.png)

<p align="center"><b>Figura 10 - </b> Wireframe - Login </p>
<p align="center">Fonte: Elaboração Grupo 4</p>


### Tela 2 e 3 - Calibração

; A tela apresenta a funcionalidade de login. Para entrar na plataforma, é necessário inserir nos inputs, respectivamente o e-mail e a senha. Além disso, é apresentada a funcionalidade de "esqueci minha senha", a qual recuperar a senha de um usuário.  


; A calibração é uma parte essencial para o funcionamento da solução, uma vez que ela permite o usuário mostrar ao robô onde deve montar os kits e retirar as peças. Para que isso ocorra, foi criado um sistema em que o usuário coloca o robô, através do uso da sua função manual, nas devidas posições.  


#### Tela 2 - Selecionar posição

; Nessa tela, existe uma simulação de uma bandeja de entrada, na qual aparecem 3 pontos cinzas para serem calibrados. O usuário deve clicar em um dos pontos para iniciar o processo de calibração do robô.

![Wireframe Calibrar](/img/wireframe-calibrar.png)

<p align="center"><b>Figura 11 - </b> Wireframe - Calibração - Selecionar ponto</p>
<p align="center">Fonte: Elaboração Grupo 4</p>

#### Tela 3 - Calibrar ponto específico


; A tela mostra em destaque o ponto selecionado pelo usuário anteriormente. A partir desse ponto, o usuário deve interagir com a garra, utilizando de seu botão, que permite mover a garra de forma manual, para colocar ela no exato ponto indicado pela tela. Ao colocar a garra exatamente onde indicado, o usuário apertará o botão de confirmar ponto e será levado de volta a tela 2, para que faça a calibração de todos os pontos necessários. 


![Wireframe Calibrar - Ponto Específico](/img/wireframe-calibrar-especifico.png)

<p align="center"><b>Figura 12 - </b> Wireframe - Calibrar manualmente robô</p>
<p align="center">Fonte: Elaboração Grupo 4</p>

### Tela 4 - Escolher o kit a ser produzido

; Ao concluir a calibração, o usuário deve escolher o kit que será produzido pelo robô. Para isso, foi idealizado uma tela similar aos motores de pesquisa na internet, no qual usuário insere caracteres e são sugeridas alternativas para ele, com a finalidade de facilitar o processo, caso ele esqueça o nome completo do kit que precisava ser executado.

![Wireframe Selecionar Kit](/img/wireframe-kit.png)

<p align="center"><b>Figura 13 - </b> Wireframe - Kit </p>
<p align="center">Fonte: Elaboração Grupo 4</p>

### Tela 5 - Confirmar quantidade do kit a ser produzido

; Nessa parte da solução, o usuário deve verificar se o kit que está sendo realizado condiz com o solicitado à ele. Assim como, ele deverá inserir a quantidade de kits que devem ser realizados pelo robô.

![Wireframe Quantidade de Kits](/img/wireframe-quantidade.png)

<p align="center"><b>Figura 14 - </b> Wireframe - Quantidade de Kits</p>
<p align="center">Fonte: Elaboração Grupo 4</p>

### Tela 6 - Kit em produção

; Essa tela representa o momento em que o braço robótico estará realizando os kits necessários. Para o usuário não ficar perdido perante o trabalho do robô, essa tela contém uma imagem com um símbolo de loading, para compreender que é necessário aguardar um momento para poder usar o sistema novamente.

![Wireframe Produção dos kits](/img/wireframe-loading.png)

<p align="center"><b>Figura 15 - </b> Wireframe - Kits em produção</p>
<p align="center">Fonte: Elaboração Grupo 4</p>


### Tela 7 - Finalização dos kits 

; Ao finalizar todos os kits solicitados pelo usuário, essa tela aparecerá e o usuário terá duas opções. Sendo assim, ou a linha de produção é iniciada novamente ou o usuário encerrará a ação no site e fechará o mesmo.   


![Wireframe Conclusão dos kits](/img/wireframe-final-kit.png)

<p align="center"><b>Figura 16 - </b> Wireframe - Tela final</p>
<p align="center">Fonte: Elaboração Grupo 4</p>
