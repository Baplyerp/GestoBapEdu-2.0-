import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URL de conexão direta com o Postgres do Supabase
SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://postgres:GestoBapEdu2026@db.seu-projeto.supabase.co:5432/postgres" 
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
