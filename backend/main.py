from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
