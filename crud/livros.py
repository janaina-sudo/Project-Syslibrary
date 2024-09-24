from sqlalchemy.orm import Session
from utils.utils import gerar_hash_senha, verificar_senha
from models.models import Livro, Leitor, Emprestimo


# inserir livros no banco de dados
def cadastrar_livro(db: Session, livro: Livro):
    #verificando se o livro já existe
    if db.query(Livro).filter(Livro.titulo == livro.titulo).first():
        return {"erro": "Livro já cadastrado"}
    
    #criando o livro
    db_livro = Livro(**livro.dict())
    db.add(db_livro)
    db.commit()
    db.refresh(db_livro)
    return db_livro


# listar todos os livros
def listar_livros(db: Session):
    if not db.query(Livro).all():
        return {"erro": "Nenhum livro encontrado"}
    
    return db.query(Livro).all()


# deletar livro
def deletar_livro(db: Session, livro_id: int):
    db_livro = db.query(Livro).filter(Livro.id == livro_id).first()
    if not db_livro:
        return {"erro": "Livro não encontrado"}
    
    db.delete(db_livro)
    db.commit()
    return {"mensagem": "Livro deletado com sucesso"}


# atualizar dados do livro
def atualizar_livro(db: Session, livro_id: int, livro: Livro):
    db_livro = db.query(Livro).filter(Livro.id == livro_id).first()
    if not db_livro:
        return {"erro": "Livro não encontrado"}
    
    livrodb = db.query(Livro).filter(Livro.id == livro_id).update(livro.dict())
    db.commit()
    #retornar dados do livro atualizado
    return db.query(Livro).filter(Livro.id == livro_id).first()


