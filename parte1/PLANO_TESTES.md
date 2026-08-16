# Plano de Testes — Parte 1

## Módulo Escolhido
O módulo escolhido foi o **`flaskbb/forum/`**.

### Justificativa
O módulo de fórum representa o núcleo de domínio do sistema (core domain), sendo responsável pela gestão de categorias, fóruns, tópicos e posts. Aumentar a confiança desse módulo é essencial antes de realizar qualquer refatoração.

## Cobertura Atual e Meta
- **Cobertura Inicial:** 5%
- **Meta de Incrememento:** Aumentar a cobertura e garantir a execução verde de testes cobrindo entidades essenciais do domínio (`Category`, `Forum`, `Topic`, `Post`).

## Lista de Cenários Selecionados
1. **Caminho Feliz:** Criação de Categoria com atributos válidos.
2. **Caminho Feliz:** Criação de Fórum vinculado a uma Categoria.
3. **Caminho Feliz:** Criação de Tópico e associação do Post inicial.
4. **Caminho Feliz:** Edição do conteúdo de um Post existente.
5. **Caso de Borda:** Alteração de visibilidade (trancar/destrancar e fixar/desfixar tópicos).
6. **Erro/Borda:** Exclusão de tópicos e validação da remoção no banco de dados.
7. **Parametrizado:** Validação de cadastro de categorias com múltiplas posições e nomes.
8. **Dublê/Mock:** Verificação da chamada do serviço de notificação por e-mail isolando dependência externa.

