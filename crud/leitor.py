from sqlalchemy.orm import Session
from utils.utils import gerar_hash_senha, verificar_senha
from models.models import Leitor, Emprestimo, leitores_livros


# cadastrar leitor
def cadastrar_leitor(db: Session, leitor: Leitor):
    
    #verificando se o leitor já existe
    if db.query(Leitor).filter(Leitor.email == leitor.email).first():
        return {"erro": "Leitor já cadastrado"}
    
    #criando o leitor
    db_leitor = Leitor(**leitor.dict())
    db_leitor.senha = gerar_hash_senha(db_leitor.senha)
    db.add(db_leitor)
    db.commit()
    db.refresh(db_leitor)
    return db_leitor

# login leitor
def login_leitor(db: Session, email: str, senha: str):
    #verificando se o leitor existe
    db_leitor = db.query(Leitor).filter(Leitor.email == email).first()
    if not db_leitor:
        return {"erro": "Leitor não encontrado"}
    
    #verificando a senha
    if not verificar_senha(senha, db_leitor.senha):
        return {"erro": "Senha incorreta"}
    
    return db_leitor



# visualizar emprestimos do leitor
def visualizar_emprestimos(db: Session, leitor_id: int):
    #verificando se o leitor existe
    db_leitor = db.query(Leitor).filter(Leitor.id == leitor_id).first()
    if not db_leitor:
        return {"erro": "Leitor não encontrado"}
    
    #verificando se o leitor possui emprestimos
    emprestimos = db.query(Emprestimo).filter(Emprestimo.leitor_id == leitor_id).all()
    if not emprestimos:
        return {"erro": "Leitor não possui emprestimos"}
    
    return emprestimos


# função que retorna os livros lidos com base na tabela associativa leitores_livros

def livros_lidos(db: Session, leitor_id: int):
    #verificando se o leitor existe
    db_leitor = db.query(Leitor).filter(Leitor.id == leitor_id).first()
    if not db_leitor:
        return {"erro": "Leitor não encontrado"}
    
    #verificando se o leitor possui livros lidos
    lista_livros = []
    livros = db.query(leitores_livros).filter(leitores_livros.c.leitor_id == leitor_id).all()
    if not livros:
        return {"erro": "Leitor não possui livros lidos"}

    leitor = db.query(Leitor).filter(Leitor.id == leitor_id).first()
    for livro in leitor.livros:
        lista_livros.append(livro.titulo)

    return lista_livros





