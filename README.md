# 🧠 Sistema Financeiro com IA — Documentação Inicial + C4 Model Unificado

Este documento consolida toda a arquitetura inicial do sistema, incluindo:

- Visão geral
- Microserviços
- Tecnologias utilizadas
- Estrutura DDD + Clean Architecture
- **Modelo C4 completo (context, containers e componentes)**
- **Código PlantUML do diagrama unificado**

---

# 1. 🎯 Visão Geral do Sistema

O sistema é uma plataforma moderna para gestão financeira com inteligência artificial, permitindo:

- Controle de transações
- Categorias personalizadas
- Gestão de planos e assinaturas
- Análise inteligente com IA (classificação automática, previsões, insights)
- Gerenciamento de usuários
- Autenticação e autorização seguras

Toda a arquitetura segue:

- **Microserviços**
- **Clean Architecture**
- **Domain-Driven Design (DDD)**
- **Banco MySQL**
- **NestJS + TypeORM**
- **FastAPI para IA**

---

# 2. 🏗️ Microserviços do Sistema

### **1. API Gateway (NestJS)**
Funções principais:
- Autenticação
- Roteamento entre serviços
- BFF (Backend For Frontend)
- Rate limiting
- Validações globais

---

### **2. Auth Service**
- Login / Logout
- Refresh tokens
- Controle de permissões

---

### **3. Users Service**
- Informações do usuário
- Perfis
- Dados pessoais

---

### **4. Categories Service**
- CRUD de categorias personalizadas  
- Vínculo com transações

---

### **5. Transactions Service**
- Lançamento de despesas e receitas
- Relatórios e extratos
- Comunicação com serviço de IA

---

### **6. Plans & Assinatura Service**
- Planos gratuitos e premium
- Assinaturas recorrentes
- Controle de limites por plano

---

### **7. IA Service (FastAPI)**
Funcionalidades:
- Classificação automática de transações
- Sugestões inteligentes
- Insights personalizados
- Previsão de gastos

---

# 3. 📦 Estrutura de Pastas (DDD + Clean Architecture)

Segue o padrão para todos os microserviços:

```txt
src
 ├── core
 │    ├── domain
 │    │     ├── entities
 │    │     ├── value-objects
 │    │     └── services
 │    ├── errors
 │    └── use-cases
 │
 ├── modules
 │    ├── <module>
 │    │    ├── application
 │    │    │     ├── dto
 │    │    │     ├── adapters
 │    │    │     └── use-cases
 │    │    ├── domain
 │    │    │     ├── entities
 │    │    │     ├── value-objects
 │    │    │     └── repositories
 │    │    └── infra
 │    │          ├── typeorm
 │    │          ├── controllers
 │    │          └── mappers
 │
 ├── infra
 │    ├── typeorm
 │    └── http
 │
 └── main.ts
