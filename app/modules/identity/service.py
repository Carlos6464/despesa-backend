from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.modules.identity.models import User
from app.modules.identity.schemas import UserCreate, UserLogin
from app.modules.identity.repository import UserRepository
from app.core.security import get_password_hash, verify_password, create_access_token

class IdentityService:
    def __init__(self):
        self.repo = UserRepository()

    def create_user(self, db: Session, user_data: UserCreate):
        # 1. Regra: Email único
        if self.repo.get_by_email(db, user_data.email):
            raise HTTPException(status_code=400, detail="Email já cadastrado.")
        
        # 2. Regra: Hash da senha
        hashed_password = get_password_hash(user_data.password)
        
        # 3. Cria o objeto do banco
        new_user = User(
            email=user_data.email,
            password_hash=hashed_password,
            role=user_data.role,
            whatsapp=user_data.whatsapp
        )
        
        return self.repo.create(db, new_user)

    def authenticate(self, db: Session, login_data: UserLogin):
        # 1. Busca usuário
        user = self.repo.get_by_email(db, login_data.email)
        
        # 2. Verifica se existe e se a senha bate
        if not user or not verify_password(login_data.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciais inválidas",
                headers={"WWW-Authenticate": "Bearer"},
            )
            
        # 3. Gera o token com o ID e o ROLE (importante para permissões futuras)
        access_token = create_access_token(data={"sub": str(user.id), "role": user.role})
        return {"access_token": access_token, "token_type": "bearer"}

identity_service = IdentityService()