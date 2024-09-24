from sqlalchemy.orm import Session
from utils.utils import gerar_hash_senha, verificar_senha
from models.models import Administrador


# inserir administrador no banco de dados
def cadastrar_administrador(db: Session, administrador: Administrador):
    #verificando se o administrador já existe
    if db.query(Administrador).filter(Administrador.email == administrador.email).first():
        return {"erro": "Administrador já cadastrado"}
    
    #criando o administrador
    db_administrador = Administrador(**administrador.dict())
    db_administrador.senha = gerar_hash_senha(db_administrador.senha)
    db.add(db_administrador)
    db.commit()
    db.refresh(db_administrador)
    return db_administrador

# login administrador
def login_administrador(db: Session, email: str, senha: str):
    #verificando se o administrador existe
    db_administrador = db.query(Administrador).filter(Administrador.email == email).first()
    if not db_administrador:
        return {"erro": "Administrador não encontrado"}
    
    #verificando a senha
    if not verificar_senha(senha, db_administrador.senha):
        return {"erro": "Senha incorreta"}
    
    return db_administrador







