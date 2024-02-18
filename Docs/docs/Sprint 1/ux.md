# Artefato de UX
## User Stories

&emsp;&emsp;As *user story* tratam-se de uma descrição simples e concisa de um recurso contado a partir da perspectiva de uma pessoa que deseja esse novo recurso, geralmente um usuário ou cliente do sistema. Elas são uma parte fundamental do desenvolvimento ágil e ajudam a criar uma visão simplificada de um requisito.<br />
&emsp;&emsp;Elas devem ser curtas e simples seguindo um formato que identifique quem será o usuário, qual será a ação executada e qual será o objetivo da ação.<br />
&emsp;&emsp;Além disso, elas devem ser:

**1. Independentes**: Cada *user story* deve ser autônoma, ou seja, deve ser possível desenvolvê-la e implementá-la independentemente das outras.

**2. Negociáveis**: Uma *user story* é uma conversa, não um contrato. Detalhes podem ser alterados e renegociados.

**3. Valiosas**: Cada *user story* deve fornecer valor ao usuário ou ao cliente.

**4. Estimáveis**: Deve ser possível estimar o esforço necessário para implementar uma *user story*.

**5. Pequenas**: *user stories* devem ser pequenas o suficiente para serem planejadas e executadas em uma iteração.

**6. Testáveis**: Cada *user story* deve ser testável para garantir que o recurso foi implementado corretamente.

&emsp;Existem ainda os **critérios de aceitação** que são um conjunto de parâmetros que definem se um produto, processo ou serviço atende aos requisitos especificados por empresas ou normas e são uma ferramenta importante para garantir que o produto final atenda às necessidades do cliente e esteja em conformidade com as normas e regulamentações aplicáveis.<br />
&emsp;Nesse contexto, seguem as *user stories* referentes a cada persona no contexto do projeto<br />

### **Persona: Renata Sanches, auxiliar de enfermagem**

&emsp;**1.** Como auxiliar de enfermagem, quero ser capaz de identificar facilmente os medicamentos corretos no sistema para garantir a administração precisa e segura.<br />
&emsp;**Critérios de Aceitação**
    - O sistema deve exibir claramente os nomes e detalhes dos medicamentos.
    - O sistema deve permitir a busca de medicamentos por nome ou código.
    - O sistema deve exibir o rastreamento dos medicamentos.

&emsp;**2.** Como auxiliar de enfermagem, quero que o software, o qual interage com o braço robótico, tenha interface da fácil usabilidade para permitir uma interação segura.<br />
&emsp;**Critérios de Aceitação**
    - O software deve ter uma interface intuitiva e fácil de usar. 
    - O hardware deve operar de maneira segura para evitar qualquer dano ao paciente ou ao auxiliar de enfermagem.
    - Deve haver recursos de treinamento disponíveis, como manuais do usuário, para ajudar os auxiliares de enfermagem a entenderem completamente o funcionamento do software e do hardware.
    
&emsp;**3.** Como auxiliar de enfermagem, quero que o sistema me permita registrar a administração de medicamentos para manter um registro preciso.<br />
&emsp;**Critérios de Aceitação**<br />
    - O sistema deve permitir o registro da data e hora da administração do medicamento.
    - O sistema deve permitir a entrada de notas adicionais, se necessário.
    - O sistema deve atualizar automaticamente o registro do paciente com as informações de administração do medicamento.
   
&emsp;**4.** Como auxiliar de enfermagem, quero que o sistema me permita visualizar o histórico de medicamentos do paciente para entender melhor seu tratamento.<br />
&emsp;**Critérios de Aceitação**
    - O sistema deve fornecer uma visão clara e organizada do histórico de medicamentos do paciente.
    - O sistema deve permitir a filtragem do histórico de medicamentos por data, tipo de medicamento, etc.
    - O sistema deve permitir o acesso a detalhes adicionais sobre cada entrada do histórico de medicamentos, se necessário.

&emsp;**5.** Como auxiliar de enfermagem, quero que o sistema me permita programar diferentes layouts de kits de emergência para que consiga adaptar os kits conforme a necessidade do paciente.<br />
&emsp;**Critérios de Aceitação**<br />
    - O sistema deve permitir que os auxiliares de enfermagem criem e salvem diferentes layouts de kits de emergência.
    - O sistema deve ser capaz de adaptar os kits de emergência com base nas necessidades específicas do paciente.
    - A interface do sistema para programar os layouts dos kits de emergência deve ser intuitiva e fácil de usar.


### **Persona: Mayumi Tanaka, gestora Hospitalar**

&emsp;**1.** Como gestora hospitalar, quero ser capaz de monitorar o abastecimento e desmontagem dos kits de emergência para garantir a eficiência do processo.<br />
&emsp;**Critérios de Aceitação**<br />
    - O sistema deve fornecer informações em tempo real sobre o status de abastecimento e desmontagem dos kits de
    emergência.
    - O sistema deve permitir a visualização do histórico de abastecimento e desmontagem.
    - O sistema deve fornecer alertas quando os níveis de suprimentos atingirem um ponto crítico.

&emsp;**2.** Como gestora hospitalar, quero que o sistema me forneça relatórios detalhados sobre o uso de medicamentos para ajudar na tomada de decisões estratégicas.<br />
&emsp;**Critérios de Aceitação**<br />
    - O sistema deve ser capaz de gerar relatórios detalhados sobre o uso de medicamentos.
    - O sistema deve permitir a personalização dos relatórios com base em diferentes parâmetros.
    - O sistema deve permitir a exportação dos relatórios para diferentes formatos.
    
&emsp;**3.** Como gestora hospitalar, quero que o hardware seja preciso e mitigue os erros de imprecisão humana que são cometidos na montagem dos kits para garantir uma maior precisão e segurança do processo.<br />
&emsp;**Critérios de Aceitação**<br />
    - O hardware deve ser capaz de montar os kits com uma precisão superior à montagem manual.
    - O hardware deve ter mecanismos de verificação incorporados para identificar e corrigir erros durante a montagem do kit.
    - O hardware deve ser capaz de manter um registro preciso de cada etapa do processo de montagem do kit.
   
&emsp;**4.** Como gestora hospitalar, quero que o sistema me permita rastrear todos os itens nos carrinhos montados para garantir a precisão e a segurança.<br />
&emsp;**Critérios de Aceitação**<br />
    - O sistema deve permitir o rastreamento de todos os itens nos carrinhos montados.
    - O sistema deve fornecer alertas se houver discrepâncias ou erros no rastreamento de itens.
    - O sistema deve permitir a correção de erros de rastreamento.

&emsp;**5.** Como gestora hospitalar, quero que o sistema me permita programar a manutenção dos carrinhos de emergência para garantir sua funcionalidade e durabilidade.<br />
&emsp;**Critérios de Aceitação**<br />
    - O sistema deve permitir a programação de manutenção para os carrinhos de emergência.
    - O código do sistema deve ser de fácil entendimento para que seja possível realizar alterações para garantir a manutenibilidade.
    - O sistema deve permitir a atualização do status de manutenção após a conclusão da manutenção.



