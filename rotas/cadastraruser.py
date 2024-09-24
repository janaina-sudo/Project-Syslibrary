from fastapi import APIRouter, Depends
from database.database import SessionLocal
from sqlalchemy.orm import Session
from crud.administrador import cadastrar_administrador
from crud.leitor import cadastrar_leitor
from schemas import schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#rota cadastrar adm
@router.post("/cadastrar_administrador")
def cadastro_administrador(administrador: schemas.AdministradorCreate, db: Session = Depends(get_db)):
    return {"Administrador cadastrado": cadastrar_administrador(db, administrador)}


#rota cadastrar leitor
@router.post("/cadastrar_leitor")
def cadastro_leitor(leitor: schemas.LeitorCreate, db: Session = Depends(get_db)):
    return {"Leitor cadastrado": cadastrar_leitor(db, leitor)}



