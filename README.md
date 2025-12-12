# 🧭 Sistema de Gestão Financeira — Arquitetura Inicial

Este projeto é um ecossistema completo baseado em **microserviços**, utilizando **NestJS + TypeORM + FastAPI**, seguindo os princípios de **DDD + Clean Architecture**.

O objetivo é criar uma plataforma robusta, modular, escalável e preparada para crescimento, com processamento inteligente de transações usando IA.

---

# 📚 Sumário

1. [Arquitetura Geral](#arquitetura-geral)
2. [Stack Tecnológica](#stack-tecnológica)
3. [Microserviços](#microserviços)
4. [Modelos C4](#modelos-c4)
   - [C1 — Contexto](#c1--contexto)
   - [C2 — Containers](#c2--containers)
   - [C3 — Componentes](#c3--componentes)
   - [C4 — Deployment](#c4--deployment)
5. [Estrutura de Pastas](#estrutura-de-pastas)
6. [Como Visualizar os Diagramas](#como-visualizar-os-diagramas)
7. [Como Rodar o Projeto](#como-rodar-o-projeto)
8. [Próximos Passos](#próximos-passos)

---

# 🏗️ Arquitetura Geral

O sistema segue:

- **Microserviços** independentes
- **API Gateway** como ponto único de entrada
- **FastAPI** para o serviço de IA de categorização
- **NestJS** com **TypeORM** para serviços de domínio
- **PostgreSQL** com schemas separados por contexto
- **DDD + Clean Architecture**
- **C4 Model** para documentação

---

# ⚙️ Stack Tecnológica

### **Backend**
- NestJS (API Gateway e microserviços)
- TypeORM
- PostgreSQL
- FastAPI (IA)

### **Frontend**
- Next.js (Web)
- React Native (Mobile)

### **Infraestrutura**
- Docker / Docker Compose
- Kubernetes (opcional)
- NGINX (Reverse Proxy externo)
- RabbitMQ (opcional para eventos)

---

# 🧩 Microserviços

| Serviço | Responsabilidade | Tech |
|--------|------------------|------|
| **Auth** | Login, tokens, permissões | NestJS + TypeORM |
| **Users** | Perfil de usuários | NestJS + TypeORM |
| **Categories** | Categorias financeiras | NestJS + TypeORM |
| **Transactions** | Transações financeiras | NestJS + TypeORM |
| **Plans** | Planos e níveis | NestJS + TypeORM |
| **Assinatura** | Assinaturas dos usuários | NestJS + TypeORM |
| **AI Service** | Categorização inteligente | FastAPI + Python |

---

# 🗺️ Modelos C4

Cada nível do modelo está separado para facilitar visualização e modificação.

---

## 🎯 **C1 — Contexto**

```wsd
@startuml C1_Context
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml

Person(user, "Usuário", "Cliente do sistema")
System_Boundary(system, "Finanças App") {

  System(apiGateway, "API Gateway", "Roteia requisições")
  System(authMS, "Auth Service")
  System(usersMS, "Users Service")
  System(categoriesMS, "Categories Service")
  System(transactionsMS, "Transactions Service")
  System(plansMS, "Plans Service")
  System(assinaturaMS, "Assinatura Service")
  System(aiMS, "AI Service (FastAPI)")
}

Rel(user, apiGateway, "Usa via app/web")
Rel(apiGateway, authMS, "Autentica")
Rel(apiGateway, usersMS, "Gerencia usuários")
Rel(apiGateway, categoriesMS, "Gerencia categorias")
Rel(apiGateway, transactionsMS, "Envia transações")
Rel(apiGateway, plansMS, "Consulta planos")
Rel(apiGateway, assinaturaMS, "Gerencia assinatura")
Rel(transactionsMS, aiMS, "Solicita análise IA")

@enduml
