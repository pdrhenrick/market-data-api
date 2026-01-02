# 🚀 MarketData API

API de alta performance para consulta de dados financeiros em tempo real (Moedas e Criptomoedas), desenvolvida com foco em arquitetura moderna, containerização e cache distribuído.

## 📋 Sobre o Projeto

Este projeto consiste em uma API RESTful que consome dados de provedores externos (AwesomeAPI), processa as informações e as entrega ao cliente final.

O grande diferencial é a implementação de **Cache com Redis**, garantindo que requisições frequentes sejam respondidas instantaneamente (milissegundos), reduzindo latência e custo de processamento.

## 🛠 Tecnologias Utilizadas

* **Python 3.11**: Linguagem base.
* **FastAPI**: Framework moderno e de alta performance para construção de APIs.
* **Redis**: Banco de dados em memória para Cache (estratégia de Cache-Aside).
* **Docker & Docker Compose**: Para containerização e orquestração dos serviços.
* **Uvicorn**: Servidor ASGI leve.
* **Pydantic**: Para validação e serialização de dados.

## ⚙️ Arquitetura e Funcionalidades

* **Cache Strategy**: Implementação de cache com TTL (Time-to-Live) de 30 segundos.
    * *Primeira chamada:* `🐢 Cache Miss` (Busca na API externa e salva no Redis).
    * *Chamadas seguintes:* `⚡ Cache Hit` (Retorna da memória instantaneamente).
* **Containerização**: O projeto é totalmente isolado em containers Docker (App + Redis).
* **Documentação Automática**: Swagger UI interativo gerado automaticamente.

## 🚀 Como Rodar o Projeto

Para executar a aplicação, você precisa ter o **Docker** instalado.

### 1. Clone o repositório
```bash
git clone [https://github.com/pdrhenrick/market-data-api.git](https://github.com/pdrhenrick/market-data-api.git)
cd market-data-api