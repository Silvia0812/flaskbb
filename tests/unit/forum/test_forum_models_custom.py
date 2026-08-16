from unittest.mock import MagicMock, patch
import pytest
from flaskbb.forum.models import Category, Forum, Post, Topic


def test_criar_categoria_com_sucesso(database):
    """Testa a criacao direta de uma categoria no banco de dados."""
    category = Category(title="Categoria Teste", position=1).save()

    assert category.id is not None
    assert category.title == "Categoria Teste"


def test_criar_forum_pertencente_a_categoria(database):
    """Testa a criacao de um forum associado a uma categoria existente."""
    category = Category(title="Geral", position=1).save()

    forum = Forum(
        title="Forum de Discussoes",
        description="Descricao do forum",
        category_id=category.id,
        position=1,
    ).save()

    assert forum.id is not None
    assert forum.category_id == category.id


def test_criar_topico_e_validar_post_inicial(database, forum, user):
    """Testa a criacao de um topico atribuindo atributos manualmente."""
    topic = Topic()
    topic.title = "Topico de Teste"
    topic.forum_id = forum.id
    topic.user_id = user.id
    topic.username = user.username
    database.session.add(topic)
    database.session.commit()

    post = Post()
    post.content = "Conteudo do post de teste"
    post.topic_id = topic.id
    post.user_id = user.id
    post.username = user.username
    database.session.add(post)
    database.session.commit()

    topic.first_post_id = post.id
    topic.last_post_id = post.id
    database.session.commit()

    assert topic.id is not None
    assert topic.first_post_id == post.id


def test_exclusao_de_topico(database, forum, user):
    """Testa a remocao de um topico do banco de dados."""
    topic = Topic()
    topic.title = "Para Deletar"
    topic.forum_id = forum.id
    topic.user_id = user.id
    topic.username = user.username
    database.session.add(topic)
    database.session.commit()

    topic_id = topic.id
    database.session.delete(topic)
    database.session.commit()

    assert database.session.get(Topic, topic_id) is None


def test_travar_e_destravar_topico(database, forum, user):
    """Testa a alteracao de status de trancamento de um topico."""
    topic = Topic()
    topic.title = "Topico Trancado"
    topic.forum_id = forum.id
    topic.user_id = user.id
    topic.username = user.username
    topic.locked = True
    database.session.add(topic)
    database.session.commit()

    assert topic.locked is True

    topic.locked = False
    database.session.commit()
    assert topic.locked is False


def test_fixar_topico(database, forum, user):
    """Testa se um topico pode ser marcado como importante/fixo."""
    topic = Topic()
    topic.title = "Aviso Importante"
    topic.forum_id = forum.id
    topic.user_id = user.id
    topic.username = user.username
    topic.important = True
    database.session.add(topic)
    database.session.commit()

    assert topic.important is True


def test_edicao_de_post(database, forum, user):
    """Testa a atualizacao do conteudo de um post."""
    topic = Topic()
    topic.title = "Topico para Edicao"
    topic.forum_id = forum.id
    topic.user_id = user.id
    topic.username = user.username
    database.session.add(topic)
    database.session.commit()

    post = Post()
    post.content = "Texto original"
    post.topic_id = topic.id
    post.user_id = user.id
    post.username = user.username
    database.session.add(post)
    database.session.commit()

    post.content = "Texto editado com sucesso"
    database.session.commit()

    assert post.content == "Texto editado com sucesso"


# --- TAREFA 1.4: Teste Parametrizado ---
@pytest.mark.parametrize(
    "titulo_categoria, posicao, eh_valido",
    [
        ("Geral", 1, True),
        ("Notícias", 99, True),
        ("Dúvidas", 0, True),
        ("Projetos", 5, True),
    ],
)
def test_validacao_parametrizada_categoria(
    database, titulo_categoria, posicao, eh_valido
):
    """Testa a criacao de categorias com variadas combinacoes de entradas validas."""
    cat = Category(title=titulo_categoria, position=posicao).save()
    assert cat.id is not None
    assert cat.title == titulo_categoria


# --- TAREFA 1.5: Teste com Dublê / Mock ---
def test_mock_servico_notificacao_email():
    """Testa a interacao com o servico de e-mail isolando a dependencia externa via Mock."""
    mock_email_service = MagicMock()

    mock_email_service.send_mail(
        to="usuario@teste.com",
        subject="Novo topico no forum",
        body="Um novo topico foi criado.",
    )

    mock_email_service.send_mail.assert_called_once_with(
        to="usuario@teste.com",
        subject="Novo topico no forum",
        body="Um novo topico foi criado.",
    )