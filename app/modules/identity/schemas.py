from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID

# Entrada: Criação de Usuário
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: str = "common" # O padrão é comum, mas permite enviar 'admin'
    whatsapp: Optional[str] = None

# Entrada: Login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Saída: O que retornamos para o Frontend (Sem a senha!)
class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    whatsapp: Optional[str] = None
    role: str
    is_active: bool

    class Config:
        from_attributes = True

# Saída: Token JWT
class Token(BaseModel):
    access_token: str
    token_type: str