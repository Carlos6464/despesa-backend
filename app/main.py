from fastapi import FastAPI
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
from app.modules.identity.router import router as identity_router

load_dotenv()

app = FastAPI(title="SaaS Despesas")
app.include_router(identity_router)

# Teste de conexão com banco na inicialização
@app.on_event("startup")
def startup():
    database_url = os.getenv("DATABASE_URL")
    try:
        engine = create_engine(database_url)
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("✅ Banco de Dados Conectado com Sucesso!")
    except Exception as e:
        print(f"❌ Erro ao conectar no banco: {e}")

@app.get("/")
def read_root():
    return {"message": "API do SaaS de Despesas está online 🚀"}