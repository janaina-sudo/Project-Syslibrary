from fastapi import APIRouter, Depends
from database.database import SessionLocal
from sqlalchemy.orm import Session
from crud.administrador import login_administrador
from crud.livros import cadastrar_livro, listar_livros, deletar_livro, atualizar_livro
from crud.emprestimo import realizar_emprestimo,  devolver_livro, get_emprestimos_leitor, renovar_emprestimo, get_emprestimo_dados
from schemas import schemas


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# rota para login administrador
@router.post("/login_administrador")
def login_usuario_administrador(administrador: schemas.AdministradorLogin, db: Session = Depends(get_db)):
    return {"Administrador logado": login_administrador(db, administrador.email, administrador.senha)}


# rota para cadastrar livro
@router.post("/cadastrar_livro")
def cadastro_livro(livro: schemas.LivroCreate, db: Session = Depends(get_db)):
    return {"Livro cadastrado": cadastrar_livro(db, livro)}


# rota para listar livros
@router.get("/listar_livros")
def listar_todos_livros(db: Session = Depends(get_db)):
    return {"Livros": listar_livros(db)}

# rota para deletar livro
@router.delete("/deletar_livro/{livro_id}")
def deletar_livro_rota(livro_id: int, db: Session = Depends(get_db)):
    return {"Livro deletado": deletar_livro(db, livro_id)}


# rota para atualizar livro
@router.put("/atualizar_livro/{livro_id}")
def atualizar_livro_rota(livro_id: int, livro: schemas.LivroUpdate, db: Session = Depends(get_db)):
    return {"Livro atualizado": atualizar_livro(db, livro_id, livro)}


# rota para realizar emprestimo
@router.post("/realizar_emprestimo")
def emprestimo(emprestimo: schemas.EmprestimoCreate, db: Session = Depends(get_db)):
    return {"Emprestimo realizado": realizar_emprestimo(db, emprestimo)}

# rota para listar todos os emprestimos feito pelo adm
@router.get("/listar_emprestimos")
def emprestimos_realizados(db: Session = Depends(get_db)):
    result = get_emprestimo_dados(db)
    return {"Emprestimos": result}

# rota para listar todos os emprestimos feito pelo leitor
@router.get("/listar_emprestimos_leitor/{leitor_id}")
def emprestimos_realizados_leitor(leitor_id: int, db: Session = Depends(get_db)):
    emp_leitor = get_emprestimos_leitor(db, leitor_id)
    return {"Emprestimos": emp_leitor}
    

# rota para devolver um livro
@router.delete("/devolver_livro/{emprestimo_id}")
def devolver_livro_rota(emprestimo_id: int, db: Session = Depends(get_db)):
    return {"Emprestimo deletado": devolver_livro(db, emprestimo_id)}  


# rota para renovar um emprestimo
@router.put("/renovar_emprestimo_adm/{emprestimo_id}")
def renovar_emprestimo_rota(emprestimo_id: int, db: Session = Depends(get_db)):
    return {"Emprestimo renovado": renovar_emprestimo(db, emprestimo_id)}

