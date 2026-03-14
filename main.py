from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, get_db
import models
import schemas

# Isso aqui substitui aquele botão vermelho de "Construir Tabelas" do Streamlit!
# Sempre que a API ligar, ela garante que as tabelas existem no Supabase.
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="GestoBapEdu 2.0 API",
    description="Backend de Alta Performance para Gestão de Estudos",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "🚀 API GestoBapEdu 2.0 está Online na Nuvem!"}

# 🚀 SEU PRIMEIRO ENDPOINT DE DADOS!
@app.get("/bancas")
def listar_bancas(db: Session = Depends(get_db)):
    # Pede para o banco listar todas as bancas
    bancas = db.query(models.Banca).all()
    return {"total": len(bancas), "bancas": bancas}
