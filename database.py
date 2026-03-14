import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# O FastAPI vai buscar aquela URL com a senha que você salvou no Render
DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("🚨 A variável DATABASE_URL não foi encontrada no Render!")

# Conecta ao Supabase
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para abrir e fechar a conexão a cada requisição (muito mais seguro e rápido que o Streamlit)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
