# Registro de Refatorações Aplicadas — Parte 2

## Refatoração 1: Extract Method em `Topic.save`
- **Hash do Commit:** *(a preencher após commit)*
- **Smell Tratado:** Long Method
- **Transformação:** Isolação da atualização de estatísticas em métodos auxiliares privados (`_update_counters`).
- **Resumo:**
  - *Antes:* O método `save()` acumulava mais de 20 linhas manipulando atributos, sessão e contadores de fórum/usuário.
  - *Depois:* Delegado o recálculo para submétodos coesos, deixando a intenção do fluxo principal direta.

## Refatoração 2: Replace Conditional with Explicit Method em Status
- **Hash do Commit:** *(a preencher após commit)*
- **Smell Tratado:** Primitive Obsession
- **Transformação:** Adição de métodos de domínio como `is_locked()` e `is_important()` em `Topic`.
- **Resumo:**
  - *Antes:* Checagens diretas nos booleans da tabela SQLAlchemy espalhadas no código.
  - *Depois:* Encapsulado em métodos com nome expressivo de negócio.

## Refatoração 3: Extract Method no Recálculo de Estatísticas
- **Hash do Commit:** *(a preencher após commit)*
- **Smell Tratado:** Duplicated Code
- **Transformação:** Unificação de chamadas de agregadores SQLAlchemy.
- **Resumo:**
  - *Antes:* Consultas agregadas de soma de tópicos repetidas em múltiplos blocos.
  - *Depois:* Reutilização de função interna para recalcular contadores de posts e tópicos.

## Refatoração 4: Replace Magic Number with Symbolic Constant
- **Hash do Commit:** *(a preencher após commit)*
- **Smell Tratado:** Magic Numbers
- **Transformação:** Definição de constantes nomeadas no topo das classes de modelos.
- **Resumo:**
  - *Antes:* Limites e valores de ordenação hardcoded diretamente nos métodos.
  - *Depois:* Constantes declaradas com significado claro (ex.: `DEFAULT_PAGE_SIZE`).