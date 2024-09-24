from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import relationship
from database.database import Base, engine

# Tabela associativa para o relacionamento NxN entre Leitor e Livro
leitores_livros = Table(
    'leitores_livros',
    Base.metadata,
    Column('leitor_id', Integer, ForeignKey('leitores.id'), primary_key=True),
    Column('livro_id', Integer, ForeignKey('livros.id'), primary_key=True)
)

# Modelo Leitor
class Leitor(Base):
    __tablename__ = "leitores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String, unique=True)
    senha = Column(String)
    endereco = Column(String)
    cpf = Column(String)
    telefone = Column(String)

    # Relacionamento NxN com Livro
    livros = relationship("Livro", secondary=leitores_livros, back_populates="leitores")

    emprestimos = relationship("Emprestimo", back_populates="leitor")


# Modelo Administrador
class Administrador(Base):
    __tablename__ = "administradores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String, unique=True)
    senha = Column(String)
    cpf = Column(String)
    
    emprestimos = relationship("Emprestimo", back_populates="administrador")


# Modelo Livro
class Livro(Base):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    autor = Column(String)
    genero = Column(String)
    status = Column(String)

    # Relacionamento NxN com Leitor
    leitores = relationship("Leitor", secondary=leitores_livros, back_populates="livros")

    emprestimos = relationship("Emprestimo", back_populates="livro")


# Modelo Emprestimo
class Emprestimo(Base):
    __tablename__ = "emprestimos"

    id = Column(Integer, primary_key=True)
    livro_id = Column(Integer, ForeignKey("livros.id"))
    leitor_id = Column(Integer, ForeignKey("leitores.id"))
    administrador_id = Column(Integer, ForeignKey("administradores.id"))
    data_emprestimo = Column(Date)
    data_devolucao = Column(Date)

    livro = relationship("Livro", back_populates="emprestimos")
    leitor = relationship("Leitor", back_populates="emprestimos")
    administrador = relationship("Administrador", back_populates="emprestimos")


# adicionando no banco de dados as tabelas
Base.metadata.create_all(bind=engine)
