
from fastapi import APIRouter, Depends
from database.database import SessionLocal
from sqlalchemy.orm import Session
from crud.leitor import  login_leitor, visualizar_emprestimos, livros_lidos
from crud.emprestimo import renovar_emprestimo
from schemas import schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# rota para login leitor
@router.post("/login_leitor")
def login_usuario_leitor(leitor: schemas.LeitorLogin, db: Session = Depends(get_db)):
    return {"Leitor logado": login_leitor(db, leitor.email, leitor.senha)}


# rota para listar todos os emprestimos feito pelo leitor
@router.get("/listar_emprestimos/{leitor_id}")
def emprestimos_realizados(leitor_id: int, db: Session = Depends(get_db)):
    return {"Emprestimos": visualizar_emprestimos(db, leitor_id)}


# rota para renovar um emprestimo
@router.put("/renovar_emprestimo/{emprestimo_id}")
def renovar_emprestimo_rota(emprestimo_id: int, db: Session = Depends(get_db)):
    return {"Emprestimo renovado": renovar_emprestimo(db, emprestimo_id)}


# rota para listar os livros lidos pelo leitor
@router.get("/livros_lidos/{leitor_id}")
def livros_lidos_rota(leitor_id: int, db: Session = Depends(get_db)):
    return {"Livros lidos": livros_lidos(db, leitor_id)}


    
    

                 


