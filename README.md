# 💰 SaaS Financeiro - Backend (FastAPI)

Backend robusto para um sistema SaaS de controle de despesas pessoais. O sistema suporta múltiplos inquilinos (multi-tenant lógico), gestão de planos de assinatura e integração via WhatsApp para lançamento rápido de despesas.

## 🚀 Visão Geral

O projeto foi construído utilizando **FastAPI** seguindo uma arquitetura de **Monolito Modular** com princípios de **DDD (Domain-Driven Design)** pragmático. O objetivo é oferecer performance, escalabilidade e fácil manutenção.

### ✨ Funcionalidades Principais

* **Autenticação & Segurança:** Login, Registro e JWT (JSON Web Tokens).
* **Gestão de Usuários:**
    * **Admin:** Cria categorias globais e gerencia o sistema.
    * **Comum:** Cria categorias pessoais e gerencia suas despesas.
* **Controle de Despesas:** CRUD completo de despesas e categorias.
* **Planos & Assinaturas:** Integração com **Stripe**.
    * **Gatekeeper:** Lógica que bloqueia recursos baseado no status do pagamento.
* **Bot de WhatsApp:** Integração via **Evolution API** + **Typebot**.
    * Lançamento de despesas por mensagem de texto.
    * **Limite Freemium:** Usuários gratuitos têm limite de 8 lançamentos via WhatsApp/mês.

---

## 🛠️ Tech Stack

* **Linguagem:** Python 3.12+
* **Framework Web:** FastAPI
* **Banco de Dados:** PostgreSQL
* **ORM:** SQLAlchemy
* **Migrações:** Alembic
* **Infraestrutura Local:** Docker & Docker Compose
* **Integrações:** Stripe (Pagamentos), Evolution API (WhatsApp Gateway)

---

## 📂 Arquitetura do Projeto

O projeto segue uma estrutura modular onde cada pasta dentro de `modules/` representa um domínio de negócio isolado.

```plaintext
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
