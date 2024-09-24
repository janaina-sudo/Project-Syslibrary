from pydantic import BaseModel
from typing import Optional
from datetime import date

# Administrador
class AdministradorBase(BaseModel):
    nome: str
    senha: str
    email: str
    cpf: str

class AdministradorCreate(AdministradorBase):
    pass

class Administrador(AdministradorBase):
    id: int

    class Config:
        from_atrributes = True


class AdministradorLogin(BaseModel):
    email: str
    senha: str



# Leitor
class LeitorBase(BaseModel):
    nome: str
    email: str
    senha: str
    endereco: str
    cpf: str
    telefone: str

class LeitorCreate(LeitorBase):
    pass 

class LeitorLogin(BaseModel):
    email: str
    senha: str


class Leitor(LeitorBase):
    id: int

    class Config:
        from_atrributes = True



# Livro
class LivroBase(BaseModel):
    titulo: str
    autor: str
    genero: str
    status: str

class LivroCreate(LivroBase):
    pass


class LivroUpdate(BaseModel):
    titulo: Optional[str]
    autor: Optional[str]
    genero: Optional[str]
    status: Optional[str]


class Livro(LivroBase):
    id: int

    class Config:
        from_attributes = True




# Emprestimo
class EmprestimoBase(BaseModel):
    livro_id: int
    leitor_id: int
    administrador_id : int
    data_emprestimo: date
    data_devolucao: date


class EmprestimoCreate(EmprestimoBase):
    pass

class Emprestimo(EmprestimoBase):
    id: int

    class Config:
        from_attributes = True


class EmprestimoUpdate(BaseModel):
    id: Optional[int]
    livro_id: Optional[int]
    leitor_id: Optional[int]
    data_emprestimo: Optional[date]
    data_devolucao: Optional[date]
    status: Optional[str]



    

