💰 SaaS Financeiro - Backend (FastAPI)
Backend robusto para um sistema SaaS de controle de despesas pessoais. O sistema suporta múltiplos inquilinos (multi-tenant lógico), gestão de planos de assinatura e integração via WhatsApp para lançamento rápido de despesas.

🚀 Visão Geral
O projeto foi construído utilizando FastAPI seguindo uma arquitetura de Monolito Modular com princípios de DDD (Domain-Driven Design) pragmático. O objetivo é oferecer performance, escalabilidade e fácil manutenção.

✨ Funcionalidades Principais
Autenticação & Segurança: Login, Registro e JWT (JSON Web Tokens).

Gestão de Usuários:

Admin: Cria categorias globais e gerencia o sistema.

Comum: Cria categorias pessoais e gerencia suas despesas.

Controle de Despesas: CRUD completo de despesas e categorias.

Planos & Assinaturas: Integração com Stripe.

Gatekeeper: Lógica que bloqueia recursos baseado no status do pagamento.

Bot de WhatsApp: Integração via Evolution API + Typebot.

Lançamento de despesas por mensagem de texto.

Limite Freemium: Usuários gratuitos têm limite de 8 lançamentos via WhatsApp/mês.

🛠️ Tech Stack
Linguagem: Python 3.12+

Framework Web: FastAPI

Banco de Dados: PostgreSQL

ORM: SQLAlchemy

Migrações: Alembic

Infraestrutura Local: Docker & Docker Compose

Integrações: Stripe (Pagamentos), Evolution API (WhatsApp Gateway)

📂 Arquitetura do Projeto
O projeto segue uma estrutura modular onde cada pasta dentro de modules/ representa um domínio de negócio isolado.

Plaintext

backend/
├── alembic/             # Migrações de Banco de Dados
├── app/
│   ├── core/            # Configurações globais (DB, Security, Settings)
│   ├── modules/         # Domínios de Negócio
│   │   ├── identity/    # Auth, Usuários, Roles
│   │   ├── finance/     # Despesas, Categorias, Relatórios
│   │   ├── subscription/# Integração Stripe e Planos
│   │   └── whatsapp/    # Webhook e Lógica do Bot
│   └── main.py          # Entrypoint da API
├── docker-compose.yml   # Orquestração de Containers
└── requirements.txt     # Dependências
⚡ Como Rodar Localmente
Pré-requisitos
Docker e Docker Compose instalados.

(Opcional) Python 3.12+ para rodar fora do Docker.

Passo 1: Configurar Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto (baseado no exemplo abaixo):

Ini, TOML

# Banco de Dados
DATABASE_URL="postgresql://saas_user:saas_password@db:5432/saas_db"

# Segurança (Gere um hash seguro: openssl rand -hex 32)
SECRET_KEY="sua_chave_secreta_aqui"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=60

# Stripe (Pagamentos)
STRIPE_API_KEY="sk_test_..."
STRIPE_WEBHOOK_SECRET="whsec_..."

# Integração WhatsApp
EVOLUTION_API_URL="https://seuservidor.com"
EVOLUTION_API_KEY="sua_api_key"
Passo 2: Rodar com Docker (Recomendado)
Este comando sobe o Banco de Dados e a API simultaneamente.

Bash

docker-compose up --build
A API estará disponível em: http://localhost:8000

Passo 3: Criar as Tabelas (Migrações)
Com o container rodando, abra um novo terminal e execute:

Bash

# Aplica as migrações do Alembic dentro do container
docker-compose exec web alembic upgrade head
📖 Documentação da API
O FastAPI gera a documentação automaticamente. Com o servidor rodando, acesse:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

🧪 Testando o Fluxo (Exemplo)
Criar Usuário: POST /auth/register

Login: POST /auth/login (Copie o access_token)

Autorizar: No Swagger, clique no cadeado 🔒 e cole o token.

Criar Categoria: POST /categories/

Lançar Despesa: POST /expenses/

🚢 Deploy
O projeto está configurado para deploy fácil em plataformas como Render ou Railway.

Configure as Variáveis de Ambiente no painel da plataforma.

Build Command: pip install -r requirements.txt

Start Command: alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port $PORT

📝 Licença
Este projeto é proprietário. Todos os direitos reservados.