# Retrospectiva do Projeto Final — Engenharia de Software II

## 1. Evolução do Módulo
Entre a Parte 1 e a Parte 3, o módulo `flaskbb/forum/` evoluiu de um estado legado com cobertura parcial de testes para uma estrutura compreensível, testada e com plano de modernização bem definido:
- **Parte 1:** Foi estabelecida uma suíte de testes automatizados sólida, cobrindo caminhos felizes, bordas e simulação de dependências via mocks.
- **Parte 2:** Foram identificados e eliminados code smells críticos, melhorando a legibilidade do código, a coesão de funções e garantindo que nenhuma regressão ocorresse.
- **Parte 3:** O módulo foi documentado em termos de contratos de interface (docstrings) e arquitetura, culminando em uma proposta sustentável de migração para o padrão de repositórios.

## 2. Aprendizados e Técnicas Utilizadas
- **Técnica mais útil:** A combinação de **Refactoring com Suporte de Testes (Parte 2)**. A garantia de ter uma suíte de testes automatizados verde permitiu realizar alterações estruturais profundas com total segurança.
- **Técnica mais desafiadora:** A **Análise de Acoplamento e Seams em Código Legado (Parte 3)**. Compreender o acoplamento implícito com o ORM SQLAlchemy e projetar abstrações limpas sem quebrar o sistema exigiu uma leitura rigorosa do código.

## 3. Análise Crítica
Se fosse recomeçar o projeto hoje, teria dedicado mais tempo ao mapeamento das dependências entre os modelos de dados na Parte 1. Isso teria agilizado a escrita de fixtures de testes mais enxutas e facilitado a identificação das abstrações necessárias para a Parte 2 e a Parte 3.
