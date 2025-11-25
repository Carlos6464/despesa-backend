import uuid
from sqlalchemy import Column, String, Boolean, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.core.database import Base
import enum

class UserRole(str, enum.Enum):
    ADMIN = "admin"
    COMMON = "common"

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    whatsapp = Column(String, unique=True, index=True, nullable=True)
    
    # Definição do Papel (Admin ou Comum)
    role = Column(String, default=UserRole.COMMON) 
    
    # Status do usuário
    is_active = Column(Boolean, default=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())