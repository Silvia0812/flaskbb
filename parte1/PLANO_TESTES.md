# Plano de Testes — Módulo Alvo (`flaskbb/forum`)

## Módulo Escolhido e Justificativa

O módulo escolhido é o **`flaskbb/forum/`**. Ele representa o domínio central da aplicação (gerenciamento de categorias, fóruns, tópicos e posts). Trata-se de uma área com lógica de negócio crítica, sendo o alvo ideal para fortalecimento da suíte de testes e posteriores refatorações de código legado.

## Cobertura Atual

- **Módulo:** `flaskbb/forum/`
- **Cobertura Inicial:** ~35%

## Meta de Incremento

- **Meta de Linhas:** Aumentar em **+15 pontos percentuais** a cobertura total do módulo `flaskbb/forum/`.
- **Meta Específica:** Cobrir caminhos de exceção/validação e regras de visibilidade/permissão em fóruns e tópicos.

## Cenários Não Cobertos a Atacar (Mínimo 6)

1. **Caminho Feliz:** Criação de tópico com tags válidas em um fórum aberto.
2. **Caminho Feliz:** Leitura e paginação de posts em um tópico com múltiplos comentários.
3. **Borda:** Tentativa de criar tópico com título excedendo o limite de caracteres permitidos.
4. **Borda:** Acesso a um fórum trancado/privado por um usuário sem permissões adequadas.
5. **Borda:** Ordenação e paginação de fórum vazio (sem tópicos cadastrados).
6. **Erro Esperado:** Edição de post por um usuário que não é o autor nem administrador (exceção de permissão).
7. **Erro Esperado:** Tentativa de mover um tópico para uma categoria/fórum inexistente.
8. **Erro Esperado:** Validação de envio de formulário com campos obrigatórios ausentes.
