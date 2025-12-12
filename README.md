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
🧱 C2 — Containers
wsd
Copiar código
@startuml C2_Containers
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

System_Boundary(authMS, "Auth Service") {
  Container(authAPI, "Auth API", "NestJS")
  ContainerDb(authDB, "Auth DB", "PostgreSQL")
}

System_Boundary(usersMS, "Users Service") {
  Container(usersAPI, "Users API", "NestJS")
  ContainerDb(usersDB, "Users DB", "PostgreSQL")
}

System_Boundary(categoriesMS, "Categories Service") {
  Container(categoriesAPI, "Categories API", "NestJS")
  ContainerDb(categoriesDB, "Categories DB", "PostgreSQL")
}

System_Boundary(transactionsMS, "Transactions Service") {
  Container(transactionsAPI, "Transactions API", "NestJS")
  ContainerDb(transactionsDB, "Transactions DB", "PostgreSQL")
}

System_Boundary(plansMS, "Plans Service") {
  Container(plansAPI, "Plans API", "NestJS")
  ContainerDb(plansDB, "Plans DB", "PostgreSQL")
}

System_Boundary(assinaturaMS, "Assinatura Service") {
  Container(assinaturaAPI, "Assinatura API", "NestJS")
  ContainerDb(assinaturaDB, "Assinatura DB", "PostgreSQL")
}

System_Boundary(aiMS, "AI Service") {
  Container(aiAPI, "FastAPI")
}

Rel(transactionsAPI, aiAPI, "Envia transação para IA")

@enduml
🧩 C3 — Componentes (Ex.: Auth Service)
wsd
Copiar código
@startuml C3_Component_Auth
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml

Container(authAPI, "Auth API", "NestJS")

Component(domain, "Domain Layer", "Entities, Value Objects, Domain Services")
Component(appLayer, "Application Layer", "Use Cases")
Component(infra, "Infra Layer", "TypeORM Repo, Controllers")
Component(controller, "AuthController")
Component(repo, "TypeORMAuthRepository")
Component(jwtService, "JwtService")

Rel(controller, appLayer, "Chama use cases")
Rel(appLayer, repo, "Repository")
Rel(appLayer, jwtService, "Gera tokens")
Rel(repo, authDB, "Lê/Escreve via TypeORM")

@enduml
☁️ C4 — Deployment (Infraestrutura)
wsd
Copiar código
@startuml C4_Deployment
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Deployment.puml

Deployment_Node(k8s, "Kubernetes Cluster") {

  Deployment_Node(gateway, "API Gateway Pod") {
    Container(apiGateway, "API Gateway", "NestJS")
  }

  Deployment_Node(authNode, "Auth Pod") {
    Container(auth, "Auth Service", "NestJS")
  }

  Deployment_Node(usersNode, "Users Pod") {
    Container(users, "Users Service", "NestJS")
  }

  Deployment_Node(categoriesNode, "Categories Pod") {
    Container(categories, "Categories Service")
  }

  Deployment_Node(transactionsNode, "Transactions Pod") {
    Container(transactions, "Transactions Service")
  }

  Deployment_Node(plansNode, "Plans Pod") {
    Container(plans, "Plans Service")
  }

  Deployment_Node(assinaturaNode, "Assinatura Pod") {
    Container(assinatura, "Assinatura Service")
  }

  Deployment_Node(aiNode, "AI Pod") {
    Container(ai, "AI Service (FastAPI)")
  }

  Deployment_Node(dbCluster, "PostgreSQL Cluster") {
    ContainerDb(mainDB, "PostgreSQL DB")
  }
}

@enduml
📂 Estrutura de Pastas
bash
Copiar código
src
 ├── core
 │    ├── domain
 │    ├── errors
 │    └── use-cases
 │
 ├── modules
 │    ├── auth
 │    ├── users
 │    ├── categories
 │    ├── transactions
 │    ├── plans
 │    └── assinatura
 │
 ├── infra
 │    ├── http
 │    └── database
 │
 └── main.ts
📌 Como visualizar os diagramas
🔹 Usando VS Code + PlantUML
Instalar extensão:

Copiar código
jebbs.plantuml
Pressionar:

mathematica
Copiar código
ALT + D
🔹 Visualizadores Online
https://plantuml.com/plantuml

https://www.planttext.com

https://kroki.io

🚀 Como rodar o projeto
bash
Copiar código
docker-compose up -d
bash
Copiar código
npm install
npm run start:dev
📈 Próximos Passos
✔ Criar repositórios dos microserviços
✔ Configurar API Gateway
✔ Implementar Auth com JWT + Refresh Token
✔ Criar Entities e Value Objects
✔ Criar o banco com TypeORM + Migrations
✔ Criar comunicação com o serviço de IA
✔ Criar documentação do domínio

