# User Stories

As user stories tratam-se de uma descrição simples e concisa de um recurso contado a partir da perspectiva de uma pessoa que deseja esse novo recurso, geralmente um usuário ou cliente do sistema. Elas são uma parte fundamental do desenvolvimento ágil e ajudam a criar uma visão simplificada de um requisito.

Elas devem ser curtas e simples seguindo um formato que identifique quem será o usuário, qual será a ação executada e qual será o objetivo da ação.

Além disso, elas devem ser:

**1. Independentes**: Cada user story deve ser autônoma, ou seja, deve ser possível desenvolvê-la e implementá-la independentemente das outras.

**2. Negociáveis**: Uma user story é uma conversa, não um contrato. Detalhes podem ser alterados e renegociados.

**3. Valiosas**: Cada user story deve fornecer valor ao usuário ou ao cliente.

**4. Estimáveis**: Deve ser possível estimar o esforço necessário para implementar uma user story.

**5. Pequenas**: user stories devem ser pequenas o suficiente para serem planejadas e executadas em uma iteração.

**6. Testáveis**: Cada user story deve ser testável para garantir que o recurso foi implementado corretamente.

Existem ainda os **critérios de aceitação** que são um conjunto de parâmetros que definem se um produto, processo ou serviço atende aos requisitos especificados por empresas ou normas e são uma ferramenta importante para garantir que o produto final atenda às necessidades do cliente e esteja em conformidade com as normas e regulamentações aplicáveis. Nesse contexto, seguem as user stories referentes a cada persona no contexto do projeto:

## **Persona: Mayumi Tanaka, gestora Hospitalar**

**1.** Como gestora hospitalar, quero ser capaz de monitorar o abastecimento e desmontagem dos kits de emergência para garantir a eficiência do processo.

**Critérios de Aceitação**
    - O sistema deve fornecer informações em tempo real sobre o status de abastecimento e desmontagem dos kits de
    emergência.
    - O sistema deve permitir a visualização do histórico de abastecimento e desmontagem.
    - O sistema deve fornecer alertas quando os níveis de suprimentos atingirem um ponto crítico.

**2.** Como gestora hospitalar, quero que o sistema me forneça relatórios detalhados sobre o uso de medicamentos para ajudar na tomada de decisões estratégicas.

**Critérios de Aceitação**
    - O sistema deve ser capaz de gerar relatórios detalhados sobre o uso de medicamentos.
    - O sistema deve permitir a personalização dos relatórios com base em diferentes parâmetros.
    - O sistema deve permitir a exportação dos relatórios para diferentes formatos.
    
**3.** Como gestora hospitalar, quero que o hardware seja preciso e mitigue os erros de imprecisão humana que são cometidos na montagem dos kits para garantir uma maior precisão e segurança do processo.

**Critérios de Aceitação**
    - O hardware deve ser capaz de montar os kits com uma precisão superior à montagem manual.
    - O hardware deve ter mecanismos de verificação incorporados para identificar e corrigir erros durante a montagem do kit.
    - O hardware deve ser capaz de manter um registro preciso de cada etapa do processo de montagem do kit.
   
**4.** Como gestora hospitalar, quero que o sistema me permita rastrear todos os itens nos kits montados para garantir a precisão e a segurança.

**Critérios de Aceitação**
    - O sistema deve permitir o rastreamento de todos os itens nos kits montados.
    - O sistema deve fornecer alertas se houver discrepâncias ou erros no rastreamento de itens.
    - O sistema deve permitir a correção de erros de rastreamento.

**5.** Como gestora hospitalar, quero que o sistema tenha um processo de remontagem eficiente e preciso para que possamos garantir a disponibilidade rápida kits, minimizar erros humanos e melhorar a qualidade do atendimento ao paciente.

**Critérios de Aceitação**
    - O sistema deve ser capaz de remontar os carrinhos de emergência de forma eficiente e precisa.
    - A remontagem dos carrinhos de emergência pelo sistema não deve resultar em erros ou omissões de itens essenciais. 
    - O processo de remontagem pelo sistema deve resultar em carrinhos de emergência prontos para uso mais rapidamente do que o processo manual atual.

## **Persona: Renata Sanches, auxiliar de enfermagem**

**1.** Como auxiliar de enfermagem, quero ser capaz de identificar facilmente os medicamentos corretos no sistema para garantir a administração precisa e segura.

**Critérios de Aceitação**
    - O sistema deve exibir claramente os nomes e detalhes dos medicamentos.
    - O sistema deve permitir a busca de medicamentos por nome ou código.
    - O sistema deve exibir o rastreamento dos medicamentos.

**2.** Como auxiliar de enfermagem, quero que o software, o qual interage com o braço robótico, tenha interface da fácil usabilidade para permitir uma interação segura.

**Critérios de Aceitação**
    - O software deve ter uma interface intuitiva e fácil de usar. 
    - O hardware deve operar de maneira segura para evitar qualquer dano ao paciente ou ao auxiliar de enfermagem.
    - Deve haver recursos de treinamento disponíveis, como manuais do usuário, para ajudar os auxiliares de enfermagem a entenderem completamente o funcionamento do software e do hardware.
    
**3.** Como auxiliar de enfermagem, quero que o sistema me permita registrar a administração de medicamentos para manter um registro preciso.

**Critérios de Aceitação**
    - O sistema deve permitir o registro da data e hora da administração do medicamento.
    - O sistema deve permitir a entrada de notas adicionais, se necessário.
    - O sistema deve atualizar automaticamente o registro do paciente com as informações de administração do medicamento.
   
**4.** Como auxiliar de enfermagem, quero que o sistema consiga se conectar aos demais softwares já utilizados pelo Hospital Sírio-Libanês para que possamos ter uma visão unificada e integrada de todas as operações.

**Critérios de Aceitação**
    - O sistema deve ser capaz de se conectar e integrar com os demais softwares já utilizados pelo Hospital Sírio-Libanês.
    - A integração do sistema com os demais softwares não deve interromper ou prejudicar as operações existentes.
    - O sistema deve fornecer uma visão unificada e integrada de todas as operações.

**5.** Como auxiliar de enfermagem, quero que o sistema me permita programar diferentes layouts de kits de emergência para que consiga adaptar os kits conforme a necessidade do paciente.

**Critérios de Aceitação**
    - O sistema deve permitir que os auxiliares de enfermagem criem e salvem diferentes layouts de kits de emergência.
    - O sistema deve ser capaz de adaptar os kits de emergência com base nas necessidades específicas do paciente.
    - A interface do sistema para programar os layouts dos kits de emergência deve ser intuitiva e fácil de usar.

## **Persona: Gabriel Menino, Auxiliar de Farmácia**

**1.** Como auxiliar de farmácia, quero que o sistema facilite a montagem dos kits hospitalares de forma automática, para reduzir o esforço físico e o risco de erros, sem a necessidade de ser significativamente mais rápido do que a montagem manual.

**Critérios de Aceitação**
    - O sistema deve ser capaz de montar automaticamente os kits hospitalares com precisão, incluindo todos os itens necessários.
     - A montagem automática deve aliviar o esforço físico dos auxiliares de farmácia, comparável ao tempo gasto na montagem manual.
     - O sistema deve minimizar os erros de montagem, proporcionando um método confiável e seguro.

**2.** Como auxiliar de farmácia, quero que o braço robótico integre um sistema de bipagem e rastreio de itens para assegurar a completa e correta montagem dos kits.

**Critérios de Aceitação**
    - Cada item adicionado ao kit pelo braço robótico deve ser bipado, garantindo sua inclusão no registro do sistema.
     - O sistema deve oferecer rastreamento preciso de todos os itens para prevenir omissões ou duplicidades.
     - Deve existir uma verificação final do kit montado para confirmar a precisão antes da liberação.
    
**3.** Como auxiliar de farmácia, desejo uma interface do sistema intuitiva e de fácil utilização para poder acompanhar e intervir no processo de montagem dos kits, se necessário.

**Critérios de Aceitação**
     - A interface do usuário deve ser simples e intuitiva, permitindo fácil acompanhamento do progresso da montagem.
     - O sistema deve oferecer feedback visual ou auditivo sobre o andamento da montagem dos kits.
     - Os usuários devem poder pausar, ajustar ou cancelar a montagem facilmente através da interface.
   
**4.** Como auxiliar de farmácia, quero um sistema que minimize a pressão por precisão na montagem dos kits, fornecendo um método confiável que reduza o risco de erros. 

**Critérios de Aceitação**
     - O sistema deve ter uma baixa taxa de erro, aumentando a confiança na precisão dos kits montados.
     - Deve haver funcionalidades para detecção e alerta de discrepâncias durante a montagem.
     - O sistema deve manter registros detalhados de cada montagem, facilitando futuras revisões e auditorias.


**5.** Como auxiliar de farmácia, preciso que o sistema se integre aos softwares de gestão de estoque da farmácia, para manter atualizadas as informações de estoque e demanda.

**Critérios de Aceitação**
     - O sistema deve ser capaz de se integrar com o software de gestão de estoque existente, mantendo a consistência das informações.
     - A integração deve oferecer uma visão completa do estoque, ajudando na gestão da demanda de kits.
     - Atualizações automáticas do estoque, baseadas nos itens usados na montagem dos kits, devem garantir que os dados de estoque sejam precisos e confiáveis.

## **Conclusão**

Essas user stories detalham claramente as necessidades das personas no ambiente hospitalar, cobrindo gestão a administração de medicamentos. Seguindo princípios ágeis e critérios de aceitação, as equipes podem eficientemente atender às demandas dos usuários. A ênfase em aspectos cruciais das user stories torna possível o desenvolvimento de softwares voltados para o usuário, aprimorando os serviços de saúde prestados pelo Hospital Sírio-Libanês.