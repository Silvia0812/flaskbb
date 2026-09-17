# Documentação Estratégica do Módulo: `flaskbb/forum/`

## 1. Propósito do Módulo
O módulo `flaskbb/forum/` atua como o coração do domínio da aplicação FlaskBB, sendo responsável pelo gerenciamento completo da estrutura hierárquica e do ciclo de vida das discussões (Categorias, Fóruns, Tópicos e Postagens). Ele engloba as regras de negócio associadas à publicação, moderação, atualização de métricas de uso e controle de permissões de leitura e escrita.

## 2. Mapa dos Arquivos Principais

| Arquivo | Responsabilidade Principal |
| :--- | :--- |
| `models.py` | Entidades ORM (`Category`, `Forum`, `Topic`, `Post`) e lógica de persistência e estatísticas. |
| `views.py` | Rotas e handlers de requisição HTTP para exibição e gerenciamento do fórum. |
| `forms.py` | Formulários WTForms para validação de entrada ao criar e editar tópicos ou postagens. |
| `services.py` | Lógica de aplicação e serviços do fórum desacoplados das views. |
| `plugins.py` | Hooks e pontos de extensão do módulo para o sistema de plugins do FlaskBB. |

## 3. Pontos de Entrada e Saída
- **Pontos de Entrada (Inputs):**
  - Requisições HTTP tratadas pelas rotas Flask em `views.py` (ex.: `/forum/<int:forum_id>`, `/topic/<int:topic_id>`).
  - Funções de serviço invocadas por outros módulos, como o painel administrativo (`flaskbb/management/`).
- **Destinos de Saída (Outputs):**
  - Entidades persistidas e atualizadas no banco de dados via SQLAlchemy (`models.py`).
  - Renderização de templates Jinja2 (`flaskbb/templates/forum/`).
  - Disparo de sinais e eventos assíncronos (`flaskbb.utils.signals`).

## 4. Docstrings Novas e Reescritas
Abaixo estão as 3 docstrings implementadas no fork (`Silvia0812/flaskbb`) para esclarecer contratos complexos:

1. **`flaskbb/forum/models.py` — Método `Topic.save()`**
   - *Motivo:* Método crítico que encapsula criação/edição, atribuição de autor, atualização de timestamps e recalculo das estatísticas do fórum pai em uma transação única.
2. **`flaskbb/forum/models.py` — Método `Forum.recompute_stats()`**
   - *Motivo:* Executa consultas agregadas para recalcular o total de tópicos, posts e último post publicado, sincronizando o estado da entidade com o banco.
3. **`flaskbb/forum/views.py` — Função `view_topic()`**
   - *Motivo:* Handler de rota denso responsável por validar permissões de leitura, incrementar contagem de visualizações e paginar os posts associados.
