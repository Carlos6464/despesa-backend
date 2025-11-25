from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.modules.identity import schemas, service

router = APIRouter(prefix="/auth", tags=["Identidade"])

@router.post("/register", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    return service.identity_service.create_user(db, user_data)

@router.post("/login", response_model=schemas.Token)
def login(login_data: schemas.UserLogin, db: Session = Depends(get_db)):
    return service.identity_service.authenticate(db, login_data)