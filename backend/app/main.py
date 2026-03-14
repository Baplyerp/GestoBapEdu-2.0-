from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="GestoBapEdu 2.0 API",
    description="Backend de Alta Performance para Gestão de Estudos e Concursos",
    version="1.0.0"
)

# Configuração de CORS (Permite que o futuro Next.js converse com esta API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Na fase de produção, colocaremos a URL do seu site aqui
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "🚀 API GestoBapEdu 2.0 está Online e Operante!"}
