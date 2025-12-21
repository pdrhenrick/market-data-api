import httpx

async def get_market_data():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,BTC-BRL"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        
    # Tratando os dados para devolver um JSON mais limpo
    return {
        "dolar": {
            "preco": data["USDBRL"]["bid"],
            "variacao": data["USDBRL"]["pctChange"] + "%"
        },
        "bitcoin": {
            "preco": data["BTCBRL"]["bid"],
            "variacao": data["BTCBRL"]["pctChange"] + "%"
        }
    }