# Catálogo de Code Smells — Parte 2

- **Arquivo analisado:** `flaskbb/forum/models.py`

## 1. Long Method
- **Localização:** `flaskbb/forum/models.py` (método `Topic.save`)
- **Trecho:**
```python
def save(self, user=None, forum=None, post=None):
    if self.id:
        db.session.add(self)
        db.session.commit()
        return self

    if user is not None:
        self.user_id = user.id
        self.username = user.username

    if forum is not None:
        self.forum_id = forum.id

    # ... acumula atualização de contadores de fórum e usuário ...