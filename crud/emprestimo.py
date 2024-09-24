from datetime import timedelta
from sqlalchemy.orm import Session
from models.models import Emprestimo, Leitor, Livro, Administrador


# realizar um emprestimo
def realizar_emprestimo(db: Session, emprestimo: Emprestimo):

    #verifica se o livro existe 
    if not db.query(Livro).filter(Livro.id == emprestimo.livro_id).first():
        return {"erro": "Livro não encontrado"}
    
    #verifica se o leitor existe
    if not db.query(Leitor).filter(Leitor.id == emprestimo.leitor_id).first():
        return {"erro": "Leitor não encontrado"}
    

    
    leitor = db.query(Leitor).filter(Leitor.id == emprestimo.leitor_id).first()
    livro = db.query(Livro).filter(Livro.id == emprestimo.livro_id).first()

    if livro.status != "disponivel":
        return {"erro": "Livro não disponível para emprestimo"}

    leitor.livros.append(livro)
    db.commit()
    
    #mudando o status do livro
    livro.status = "emprestado"
    db.commit()
    
    #criando o emprestimo
    db_emprestimo = Emprestimo(**emprestimo.dict())
    db.add(db_emprestimo)
    db.commit()
    db.refresh(db_emprestimo)
    return db_emprestimo


# listar dados do emprestimo utilizando join
def get_emprestimo_dados(db: Session):
    emprestimos = (
        db.query(
            Emprestimo.id,
            Livro.titulo.label("titulo_livro"),
            Leitor.nome.label("nome_leitor"),
            Administrador.nome.label("nome_administrador"),
            Emprestimo.data_emprestimo,
            Emprestimo.data_devolucao
        )
        .join(Livro, Emprestimo.livro_id == Livro.id)
        .join(Leitor, Emprestimo.leitor_id == Leitor.id)
        .join(Administrador, Emprestimo.administrador_id == Administrador.id)
        .all()
    )

    # Convertendo resultados para lista de dicionários
    emprestimo_list = []
    for emprestimo in emprestimos:
        emprestimo_list.append({
            "id": emprestimo.id,
            "titulo_livro": emprestimo.titulo_livro,
            "nome_leitor": emprestimo.nome_leitor,
            "nome_administrador": emprestimo.nome_administrador,
            "data_emprestimo": emprestimo.data_emprestimo,
            "data_devolucao": emprestimo.data_devolucao,
        })

    return emprestimo_list



# listar todos os emprestimos realizados a um leitor
def get_emprestimos_leitor(db: Session, leitor_id: int):
    #verificando se o leitor existe
    if not db.query(Leitor).filter(Leitor.id == leitor_id).first():
        return {"erro": "Leitor não encontrado"}
    
    #verificando se o leitor possui emprestimos
    emprestimos_leitor = (
        db.query(
            Emprestimo.id,
            Livro.titulo.label("titulo_livro"),
            Emprestimo.data_emprestimo,
            Emprestimo.data_devolucao
        )
        .join(Livro, Emprestimo.livro_id == Livro.id)
        .filter(Emprestimo.leitor_id == leitor_id)
        .all()
    )

    # Convertendo resultados para lista de dicionários
    emprestimo_list = []
    for emprestimo in emprestimos_leitor:
        emprestimo_list.append({
            "id": emprestimo.id,
            "titulo_livro": emprestimo.titulo_livro,
            "data_emprestimo": emprestimo.data_emprestimo,
            "data_devolucao": emprestimo.data_devolucao,
        })

    return emprestimo_list

# devolver um livro
def devolver_livro(db: Session, emprestimo_id: int):
    #verificando se o emprestimo existe
    if not db.query(Emprestimo).filter(Emprestimo.id == emprestimo_id).first():
        return {"erro": "Emprestimo não encontrado"}

    # muda o status do livro para disponivel
    emprestimo = db.query(Emprestimo).filter(Emprestimo.id == emprestimo_id).first()
    livro = db.query(Livro).filter(Livro.id == emprestimo.livro_id).first()

    livro.status = "disponivel"
    db.commit()

    #deletando o emprestimo
    db.query(Emprestimo).filter(Emprestimo.id == emprestimo_id).delete()
    db.commit()
    return {"mensagem": "Livro devolvido com sucesso"}


# renovar um emprestimo
def renovar_emprestimo(db: Session, emprestimo_id: int):
    #verificando se o emprestimo existe
    db_emprestimo = db.query(Emprestimo).filter(Emprestimo.id == emprestimo_id).first()
    if not db_emprestimo:
        return {"erro": "Emprestimo não encontrado"}
    
    #renovando o emprestimo
    db_emprestimo.data_devolucao = db_emprestimo.data_devolucao + timedelta(days=7)
    db.commit()
    db.refresh(db_emprestimo)
    return db_emprestimo


