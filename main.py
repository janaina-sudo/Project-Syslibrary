from fastapi import FastAPI
from rotas import leitor, administrador, cadastraruser
import uvicorn

app = FastAPI()

@app.get("/", tags=["Root"])
def read_root():
    return {"Bem-vindo": "Sistema de Biblioteca"}

app.include_router(leitor.router, tags=["Leitor"])
app.include_router(administrador.router, tags=["Administrador"])
app.include_router(cadastraruser.router, tags=["Cadastrar"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)