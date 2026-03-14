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

# 🚀 ENDPOINT: Listar as missões do Radar
@app.get("/radar", response_model=list[schemas.ConcursoRadarOut])
def listar_missoes_radar(db: Session = Depends(get_db)):
    missoes = db.query(models.ConcursoRadar).order_by(models.ConcursoRadar.data_prova.asc()).all()
    return missoes

# 🚀 ENDPOINT: Criar uma nova missão no Radar
@app.post("/radar", response_model=schemas.ConcursoRadarOut)
def criar_missao_radar(missao: schemas.ConcursoRadarCreate, db: Session = Depends(get_db)):
    nova_missao = models.ConcursoRadar(
        # Por enquanto estamos criando sem o user_id (UUID) para simplificar o teste. 
        # Na Fase de Autenticação, pegaremos o usuário logado!
        nome=missao.nome,
        banca_id=missao.banca_id,
        orgao_id=missao.orgao_id,
        status=missao.status,
        prioridade=missao.prioridade,
        data_prova=missao.data_prova
    )
    db.add(nova_missao)
    db.commit()
    db.refresh(nova_missao)
    return nova_missao
