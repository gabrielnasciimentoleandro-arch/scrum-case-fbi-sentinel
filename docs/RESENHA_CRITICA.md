# Scrum no FBI: uma análise crítica do Projeto Sentinel

**Autor:** 0Barone  
**Desafio:** Scrum — Analisando Cases de Sucesso  
**Caso escolhido:** FBI Sentinel  
**Data:** outubro de 2026

## Resumo

O Projeto Sentinel modernizou o gerenciamento de informações investigativas do Federal Bureau of Investigation (FBI), substituindo fluxos fortemente dependentes de papel por um sistema eletrônico. Depois de atrasos, custos elevados e dificuldades técnicas sob uma condução predominantemente tradicional, o FBI assumiu maior controle do desenvolvimento e adotou uma abordagem ágil, descrita em relatos de praticantes como baseada em Scrum. O sistema foi implantado para todos os funcionários em julho de 2012. Esta resenha sustenta que ciclos curtos, demonstrações frequentes, priorização por valor, proximidade com usuários e liderança capaz de remover impedimentos foram decisivos para a recuperação. Contudo, o sucesso não pode ser atribuído somente ao Scrum: internalização da equipe, redução de dependências contratuais, reaproveitamento de ativos, mudança de escopo, modernização de infraestrutura e forte patrocínio executivo também contribuíram. Além disso, números promocionais de economia precisam ser confrontados com auditorias oficiais, que registram custos não incluídos em algumas estimativas e limitações posteriores de usabilidade. O caso demonstra o valor do empirismo, mas também alerta contra narrativas simplificadas de transformação ágil.

**Palavras-chave:** Scrum; agilidade; FBI; Sentinel; gestão de projetos; transformação digital; setor público.

## 1. Introdução

Grandes projetos públicos de tecnologia operam sob restrições que raramente aparecem em exemplos didáticos: contratação complexa, fiscalização externa, sistemas legados, segurança, auditoria, mudanças regulatórias e milhares de usuários. O Sentinel, sistema de informações e gerenciamento de casos do FBI, reúne todos esses fatores e tornou-se um dos casos mais citados sobre recuperação de projetos com métodos ágeis.

A narrativa popular costuma ser simples: um projeto tradicional fracassou, o Scrum foi adotado e, em pouco tempo, o sistema ficou pronto com enorme economia. Essa explicação é atraente, porém incompleta. Uma análise crítica deve separar fatos documentados, relatos de praticantes e inferências. Também deve perguntar se o FBI aplicou integralmente o framework Scrum ou se combinou práticas de Scrum com uma transformação organizacional mais ampla.

A tese desta resenha é que o empirismo associado ao Scrum contribuiu de maneira relevante para a virada do Sentinel, sobretudo ao encurtar ciclos de feedback e aproximar desenvolvimento e operação. Entretanto, o resultado decorreu de um conjunto de mudanças técnicas, contratuais e gerenciais. O caso é valioso não porque prova que um framework resolve qualquer crise, mas porque mostra que transparência, inspeção e adaptação funcionam quando a organização também modifica as condições que impedem a entrega.

Este texto foi elaborado especificamente para o projeto, por meio da comparação entre fontes independentes e institucionais. Não reproduz a análise apresentada em aula nem transforma materiais didáticos em resumo. Dados e ideias de terceiros são identificados nas referências; a seleção das evidências, os contrapontos e a conclusão constituem uma síntese crítica autoral.

## 2. Contexto e problema

O Sentinel foi concebido para substituir sistemas antigos de gerenciamento de casos e superar o fracasso do Virtual Case File (VCF). Em 2006, o FBI iniciou o programa com estimativa de **US$ 425 milhões** e conclusão prevista para dezembro de 2009. Auditorias anteriores já alertavam que estimativas de custo e prazo não eram suficientemente confiáveis e omitiam componentes relevantes, como alguns custos governamentais e de atualização tecnológica.[^1]

O modelo inicial dividia o trabalho em grandes fases e dependia intensamente de contratos e integrações complexas. Apesar de o FBI ter adotado controles de aquisição e gestão, surgiram dificuldades de pessoal especializado, integração de produtos comerciais, requisitos transferidos entre fases, cronogramas pouco transparentes e atrasos na validação com usuários.[^2]

Segundo o relatório do Office of the Inspector General (OIG) de 2012, quando a segunda fase foi aceita, aproximadamente **US$ 405 milhões** já haviam sido gastos e aquela fase estava cerca de 32% acima de seu orçamento. O valor total autorizado havia subido para **US$ 451 milhões**.[^3] Portanto, a crise não resultou apenas de “usar Waterfall”; envolveu governança, contratos, arquitetura, estimativas e alinhamento com o trabalho real dos agentes.

Essa distinção importa. O predecessor VCF e o Sentinel fazem parte da mesma história de modernização, mas não são o mesmo projeto. Frases como “dez anos de projeto fracassado” normalmente agregam iniciativas diferentes e simplificam a cronologia.

## 3. A mudança de abordagem

Em 2010, diante de desempenho insatisfatório, o FBI interrompeu parte do modelo anterior, aumentou o controle interno e escolheu uma abordagem de desenvolvimento ágil. Em resposta pública ao OIG, o órgão afirmou que reduziria a dependência de contratados tradicionais, trabalharia diretamente com especialistas de produto e priorizaria as funções de maior impacto para agentes e analistas.[^4]

Fontes ligadas à comunidade Scrum descrevem uma equipe menor, trabalho organizado em ciclos de duas semanas, backlog priorizado, incrementos demonstráveis e apresentações frequentes aos usuários. No relato de Jeff Sutherland, as demonstrações a cada Sprint foram o elemento mais poderoso na visão da liderança do projeto, porque permitiam testar resultados concretos com quem utilizaria o sistema.[^5]

Essas práticas refletem os três pilares do empirismo definidos no Scrum Guide:

- **transparência:** trabalho, progresso e problemas tornaram-se mais visíveis;
- **inspeção:** incrementos eram demonstrados e avaliados com frequência;
- **adaptação:** prioridades e soluções eram ajustadas a partir do aprendizado.[^6]

A mudança também atacou impedimentos fora do código. Decisões foram aproximadas da equipe, dependências contratuais foram reduzidas, especialistas trabalharam de maneira mais integrada e a liderança assumiu responsabilidade direta pela remoção de obstáculos. Ou seja, não houve apenas a introdução de cerimônias: houve uma alteração no sistema de gestão.

## 4. Elementos de Scrum identificados

### 4.1 Sprints e incrementos utilizáveis

Ciclos curtos limitaram o risco de permanecer meses construindo algo sem validação. A cada intervalo, a equipe precisava demonstrar software integrado e próximo de uma condição utilizável. Isso contrastava com grandes fases nas quais problemas poderiam permanecer ocultos até testes tardios.

### 4.2 Backlog priorizado por valor

A equipe passou a concentrar energia nas capacidades essenciais. Em vez de tratar todos os requisitos como igualmente urgentes, priorizou funções capazes de melhorar o trabalho investigativo. Essa escolha é compatível com a responsabilidade do Product Owner de maximizar valor, embora os documentos públicos não permitam identificar com precisão quem exerceu formalmente cada accountability do Scrum.

### 4.3 Feedback de usuários

Agentes e analistas avaliaram os incrementos. O feedback frequente reduziu a distância entre especificação e uso real, além de tornar defeitos e problemas de usabilidade visíveis antes da implantação geral. O GAO identifica feedback frequente, demonstração de valor ao fim de cada iteração e acompanhamento diário visível como práticas efetivas em projetos ágeis federais.[^7]

### 4.4 Equipe menor e mais integrada

Reduzir interfaces desnecessárias tornou a comunicação mais direta. Uma equipe menor não é automaticamente mais eficiente, mas pode diminuir filas decisórias e facilitar responsabilidade compartilhada. Para isso funcionar, foi necessário dar autonomia e acesso a especialistas — condições coerentes com uma equipe Scrum multifuncional e autogerenciável.

### 4.5 Remoção ativa de impedimentos

A liderança não se limitou a cobrar velocidade. Ela precisou enfrentar contratos, infraestrutura, decisões de arquitetura e disponibilidade de pessoas. Essa atuação se aproxima do serviço de um Scrum Master, ainda que, novamente, os registros não comprovem uma implementação canônica de todas as responsabilidades do framework.

## 5. Resultados alcançados

O FBI anunciou que o Sentinel foi disponibilizado a todos os funcionários em **1º de julho de 2012**. O sistema passou a oferecer entrada, revisão, aprovação, pesquisa e compartilhamento eletrônico de informações de casos, substituindo processos dependentes de papel.[^8]

O relatório do OIG de setembro de 2012 reconheceu que a abordagem ágil reduziu o ritmo de gastos de desenvolvimento. O Departamento de Justiça informou custo estimado de **US$ 441 milhões** para a implantação, abaixo dos US$ 451 milhões disponíveis.[^3] Entretanto, a mesma auditoria advertiu que esse valor não incluía dois anos de operação e manutenção originalmente presentes no escopo, nem todos os custos de funcionários do FBI. Assim, “abaixo do orçamento” é verdadeiro apenas quando se considera a fronteira de custo usada naquele relatório.

Em 2014, o OIG registrou que a maioria dos usuários pesquisados percebia impacto positivo na produtividade e no compartilhamento de informações. Ao mesmo tempo, encontrou insatisfação com busca e indexação: apenas 42% dos respondentes que utilizavam a busca disseram encontrar frequentemente os resultados necessários. O orçamento acumulado também havia aumentado para **US$ 551,4 milhões**, incluindo operação, manutenção e novas funcionalidades posteriores à versão 1.0.[^9]

Esses dados não anulam a recuperação. Eles apenas mostram que implantação, valor e qualidade são dimensões distintas. Um produto pode ser entregue, gerar benefícios reais e ainda exigir evolução significativa.

## 6. Análise crítica

### 6.1 O que funcionou

O maior ganho foi transformar hipóteses em evidências em intervalos curtos. Demonstrações frequentes impediram que relatórios de progresso substituíssem software funcionando. A participação de usuários melhorou a aderência operacional, enquanto a priorização reduziu dispersão. A decisão de trazer conhecimento e controle para dentro do FBI também diminuiu o custo de coordenação com múltiplos fornecedores.

O caso reforça que Scrum é mais efetivo quando a organização aceita mudar suas próprias regras. Uma equipe não se torna ágil se cada adaptação depende de longas renegociações, se usuários não participam ou se a liderança mede progresso por documentos produzidos. O Sentinel avançou porque o ambiente passou a permitir ciclos de inspeção e adaptação.

### 6.2 O que não pode ser creditado apenas ao Scrum

Vários fatores aconteceram simultaneamente:

1. maior condução interna pelo FBI;
2. redução da dependência de contratos tradicionais;
3. reutilização de componentes e trabalho anterior;
4. priorização ou transferência de requisitos;
5. atualização de hardware e infraestrutura;
6. apoio executivo e decisões mais rápidas;
7. experiência acumulada após erros anteriores.

Sem controlar essas variáveis, não é possível afirmar que o Scrum, isoladamente, causou todo o resultado. O próprio OIG registrou incertezas sobre custos, critérios de conclusão e requisitos modificados ou transferidos.[^3]

### 6.3 O problema da “economia de 90%”

Textos promocionais frequentemente afirmam que o FBI concluiu o sistema por cerca de US$ 30 milhões e economizou mais de 90%. Esse número se refere principalmente ao esforço restante depois de centenas de milhões já investidos e costuma ser comparado a projeções de continuidade do modelo anterior. Ele não representa o custo total do Sentinel.

As auditorias oficiais oferecem uma visão mais cautelosa: aproximadamente US$ 432 milhões dos US$ 451 milhões disponíveis haviam sido obrigados até a implantação da versão 1.0, e custos posteriores elevaram o orçamento acumulado.[^9] Portanto, a afirmação pode ilustrar eficiência relativa na etapa final, mas não deve ser apresentada como custo integral nem como prova isolada de retorno financeiro.

### 6.4 Scrum ou “Agile com práticas de Scrum”?

O FBI declarou oficialmente ter adotado uma abordagem ágil. Relatos de Sutherland descrevem Sprints de duas semanas, backlog, demonstrações e remoção de impedimentos. Ainda assim, as fontes públicas não documentam de forma completa Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective, Product Goal, Sprint Goal, Definition of Done e as três accountabilities conforme o Scrum Guide atual.

A classificação mais responsável é **transformação ágil fortemente influenciada por Scrum**. Chamar o caso de “Scrum puro” seria afirmar mais do que as evidências permitem. Essa cautela não reduz seu valor; ao contrário, melhora a qualidade da análise.

### 6.5 Limitações após a entrega

A auditoria de 2014 indica que usuários ainda enfrentavam problemas em busca, indexação e integração com outros sistemas. Isso demonstra que uma Definition of Done precisa incluir não apenas funcionamento técnico, mas desempenho, experiência do usuário, segurança, integração e capacidade operacional. Também reforça que o Product Backlog continua existindo após a primeira implantação.

## 7. Lições aplicáveis a outros projetos

1. **Entregar em partes reduz risco, não responsabilidade.** Iterações curtas precisam manter qualidade, segurança e rastreabilidade.
2. **Demonstração vale mais que percentual subjetivo.** Software funcionando permite inspeção concreta.
3. **Usuário precisa participar continuamente.** Feedback tardio transforma divergências em retrabalho caro.
4. **Priorizar significa escolher o que não fazer agora.** Backlog não é uma lista em que tudo possui prioridade máxima.
5. **Agilidade exige mudanças de governança.** Contratos, aprovações e métricas precisam apoiar ciclos curtos.
6. **Liderança deve remover impedimentos.** Cobrar velocidade sem eliminar bloqueios apenas aumenta pressão.
7. **Custo deve ser analisado pelo ciclo de vida.** Desenvolvimento, pessoal, infraestrutura, manutenção e evolução não podem ser misturados ou omitidos conforme a narrativa desejada.
8. **Implantação não encerra o produto.** Métricas de uso e satisfação devem orientar novas melhorias.
9. **Não se deve confundir correlação com causalidade.** Scrum pode contribuir fortemente sem ser a única causa do sucesso.

## 8. Conclusão

O Sentinel é um caso relevante de recuperação de projeto porque mostra uma organização pública adotando ciclos curtos, feedback frequente, priorização e maior autonomia para enfrentar um sistema crítico. A implantação em 2012, depois de anos de dificuldades, demonstra que práticas empíricas podem produzir valor mesmo em ambientes regulados e complexos.

Contudo, a principal lição não é que “Scrum salva qualquer projeto”. A recuperação dependeu de combinar práticas ágeis com mudanças de equipe, contratos, liderança, infraestrutura e escopo. Auditorias posteriores também revelam custos e limitações que narrativas celebratórias tendem a omitir.

Portanto, o sucesso do Sentinel deve ser entendido como uma transformação sociotécnica: Scrum forneceu um ritmo de transparência, inspeção e adaptação, mas a organização precisou criar condições reais para que esse ritmo funcionasse. Essa interpretação é mais útil para futuros projetos do que atribuir o resultado a cerimônias ou a um único framework.

---

## Referências

[^1]: U.S. GOVERNMENT ACCOUNTABILITY OFFICE. *Information Technology: FBI Following a Number of Key Acquisition Practices on New Case Management System but Improvements Still Needed*. GAO-07-912, 2007. Disponível em: <https://www.gao.gov/products/gao-07-912>.

[^2]: U.S. DEPARTMENT OF JUSTICE, OFFICE OF THE INSPECTOR GENERAL. *OIG Audit Report 07-40: The Federal Bureau of Investigation's Implementation of the Sentinel Project*. 2007. Disponível em: <https://oig.justice.gov/archives/reports/FBI/a0740/findings.htm>.

[^3]: U.S. DEPARTMENT OF JUSTICE, OFFICE OF THE INSPECTOR GENERAL. *Interim Report on the FBI's Implementation of the Sentinel Project*. Report 12-38, 2012. Disponível em: <https://www.oversight.gov/sites/default/files/documents/reports/2018-02/a1238.pdf>.

[^4]: FEDERAL BUREAU OF INVESTIGATION. *Response to OIG Report on the FBI's Sentinel Project*. 2010. Disponível em: <https://www.fbi.gov/news/pressrel/press-releases/mediaresponse_102010>.

[^5]: SUTHERLAND, Jeff. *Scrum: The Art of Doing Twice the Work in Half the Time* — trecho “Fixing the FBI”. 2014. Trecho disponibilizado em: <https://res.infoq.com/articles/sutherland-scrum-twice-work-half-time/en/resources/Book-Excerpt.pdf>.

[^6]: SCHWABER, Ken; SUTHERLAND, Jeff. *The Scrum Guide*. 2020. Disponível em: <https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf>.

[^7]: U.S. GOVERNMENT ACCOUNTABILITY OFFICE. *Software Development: Effective Practices and Federal Challenges in Applying Agile Methods*. GAO-12-681, 2012. Disponível em: <https://www.gao.gov/products/gao-12-681>.

[^8]: FEDERAL BUREAU OF INVESTIGATION. *FBI Announces Deployment of Sentinel*. 31 jul. 2012. Disponível em: <https://archives.fbi.gov/archives/news/pressrel/press-releases/fbi-announces-deployment-of-sentinel>.

[^9]: U.S. DEPARTMENT OF JUSTICE, OFFICE OF THE INSPECTOR GENERAL. *Audit of the Status of the Federal Bureau of Investigation's Sentinel Program*. Report 14-31, 2014. Disponível em: <https://oig.justice.gov/reports/audit-status-federal-bureau-investigations-sentinel-program>.
