from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Molde para CRIAR uma nova missão no Radar (O que o Frontend manda)
class ConcursoRadarCreate(BaseModel):
    nome: str
    banca_id: Optional[int] = None
    orgao_id: Optional[int] = None
    status: str
    prioridade: str
    data_prova: Optional[datetime] = None

# Molde para LER as missões (O que a API devolve para o Frontend)
class ConcursoRadarOut(BaseModel):
    id: int
    nome: str
    status: str
    prioridade: str
    data_prova: Optional[datetime]
    
    class Config:
        from_attributes = True
