from fastapi import FastAPI
from app.services import get_market_data
from app.schemas import CotacaoOutput 

# Configuração da API
app = FastAPI(
    title="MarketData API",
    description="API de dados financeiros em tempo real.",
    version="1.0.0"
)

# Rota Principal
@app.get("/")
async def root():
    return {"status": "online", "message": "MarketData API is running!"}

# Rota de Cotações (agora blindada com o Schema)
@app.get("/cotacoes", response_model=CotacaoOutput)
async def listar_cotacoes():
    """
    Retorna a cotação atual do Dólar e Bitcoin.
    """
    dados = await get_market_data()
    return dados