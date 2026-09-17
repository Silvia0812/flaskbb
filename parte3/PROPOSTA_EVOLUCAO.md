# Proposta de Evolução: Substituição da Camada de Persistência por Repositórios

## 1. Motivação
A análise legada identificou que o módulo `forum/` possui chamadas diretas ao SQLAlchemy dentro das Views HTTP e regras de negócio espalhadas em `models.py`. Essa abordagem prejudica a testabilidade, viola a separação de responsabilidades e impede a troca ou otimização da camada de dados sem impactar as rotas da aplicação.

## 2. Estado-Alvo

### Diagrama de Componentes
```mermaid
graph TD
    subgraph Presentation Layer
        VIEWS[forum/views.py]
    end

    subgraph Service Layer
        SERVICE[forum/services.py]
    end

    subgraph Data Access Layer
        REPO_INT[AbstractForumRepository]
        REPO_IMPL[SQLAlchemyForumRepository]
    end

    subgraph Persistence Layer
        MODELS[forum/models.py]
        DB[(Database)]
    end

    VIEWS --> SERVICE
    SERVICE --> REPO_INT
    REPO_IMPL -.-|Implements| REPO_INT
    REPO_IMPL --> MODELS
    MODELS --> DB
