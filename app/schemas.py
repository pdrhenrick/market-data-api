from pydantic import BaseModel

# O "Molde" de como uma moeda deve se parecer
class MoedaResponse(BaseModel):
    preco: str
    variacao: str

# O "Molde" da resposta completa da API
class CotacaoOutput(BaseModel):
    dolar: MoedaResponse
    bitcoin: MoedaResponse
    
    class Config:
        # Isso ajuda a documentação a mostrar um exemplo real
        json_schema_extra = {
            "example": {
                "dolar": {"preco": "5.15", "variacao": "0.10%"},
                "bitcoin": {"preco": "250000.00", "variacao": "-1.2%"}
            }
        }