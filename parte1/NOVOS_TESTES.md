# Mapeamento dos Novos Testes Criados

Arquivo de implementação: `tests/unit/forum/test_forum_models_custom.py`

## Tarefa 1.3 — Testes Unitários (Felizes, Bordas e Erros)
1. `test_criar_categoria_com_sucesso` — **Caminho Feliz**: Criação direta de categoria no banco.
2. `test_criar_forum_pertencente_a_categoria` — **Caminho Feliz**: Associação entre fórum e categoria.
3. `test_criar_topico_e_validar_post_inicial` — **Caminho Feliz**: Atribuição de post inicial a um tópico.
4. `test_exclusao_de_topico` — **Erro/Borda**: Remoção de tópico e asserção de ausência no banco.
5. `test_travar_e_destravar_topico` — **Caso de Borda**: Alteração da propriedade `locked`.
6. `test_fixar_topico` — **Caso de Borda**: Alteração da propriedade `important`.
7. `test_edicao_de_post` — **Caminho Feliz**: Atualização de campo `content`.

## Tarefa 1.4 — Teste Parametrizado
- **Função:** `test_validacao_parametrizada_categoria`
- **Técnica:** `@pytest.mark.parametrize`
- **Valores testados:** 4 combinações de títulos e posições (`Geral`, `Notícias`, `Dúvidas`, `Projetos`).

## Tarefa 1.5 — Teste com Dublê / Mock
- **Função:** `test_mock_servico_notificacao_email`
- **Técnica:** `unittest.mock.MagicMock`
- **Justificativa:** O dublê foi necessário para isolar a dependência do envio real de e-mails, permitindo validar o contrato de interação (`send_mail`) sem realizar chamadas de rede ou depender de um servidor SMTP configurado.

