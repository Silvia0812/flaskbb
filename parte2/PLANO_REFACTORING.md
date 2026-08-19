# Plano de Refactoring — Parte 2

## Smells Selecionados para Refatoração

### 1. Long Method em `Topic.save`
- **Refatoração:** *Extract Method* (Fowler)
- **Resultado Esperado:** Isolar a atualização de contadores do usuário e fórum em métodos auxiliares privados (`_update_counters`).
- **Riscos Antecipados:** Efeito colateral na persistência se a sessão do SQLAlchemy for finalizada antes da hora.

### 2. Duplicated Code no Recálculo de Estatísticas
- **Refatoração:** *Extract Method / Form Template Method* (Fowler)
- **Resultado Esperado:** Unificar a lógica de atualização de contadores de tópicos e posts.
- **Riscos Antecipados:** Alteração involuntária na contagem agregada de fóruns pai/filho.

### 3. Primitive Obsession em Checagens de Status
- **Refatoração:** *Replace Conditional with Explicit Method* (Fowler)
- **Resultado Esperado:** Encapsular checagens diretas de atributos como `locked` e `important` em métodos com intenção clara de domínio.
- **Riscos Antecipados:** Mínimo, mantendo compatibilidade com propriedades existentes.

### 4. Magic Numbers / Repetição de Valores Padrão
- **Refatoração:** *Replace Magic Number with Symbolic Constant* (Fowler)
- **Resultado Esperado:** Substituir valores fixos de limites e ordens por constantes nomeadas no topo da classe.
- **Riscos Antecipados:** Nenhum risco de comportamento.