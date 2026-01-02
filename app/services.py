import httpx
import json
import redis.asyncio as redis # Biblioteca assíncrona do Redis

# Conecta ao container do Redis (o nome 'redisdb' vem do docker-compose.yml)
redis_client = redis.Redis(host='redisdb', port=6379, db=0, decode_responses=True)

async def get_market_data():
    # 1. Primeiro, tenta pegar do Cache (Memória)
    cache = await redis_client.get("dados_mercado")
    
    if cache:
        print("⚡ CACHE HIT! Entregando dados instantâneos.")
        return json.loads(cache)
        
    print("🐢 CACHE MISS. Buscando dados novos na Internet...")
    
    # 2. Se não tiver no cache, busca na API externa
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,BTC-BRL"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        
    # 3. Formata os dados
    resultado = {
        "dolar": {
            "preco": data["USDBRL"]["bid"],
            "variacao": data["USDBRL"]["pctChange"] + "%"
        },
        "bitcoin": {
            "preco": data["BTCBRL"]["bid"],
            "variacao": data["BTCBRL"]["pctChange"] + "%"
        }
    }
    
    # 4. Salva no Cache por 30 segundos (TTL)
    await redis_client.set("dados_mercado", json.dumps(resultado), ex=30)
    
    return resultado