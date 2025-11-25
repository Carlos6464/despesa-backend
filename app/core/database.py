from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# Cria o Engine de conexão com o Postgres
engine = create_engine(settings.DATABASE_URL)

# Cria a fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para os Models
Base = declarative_base()

# Dependência para injetar o banco nas rotas (Dependency Injection)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()