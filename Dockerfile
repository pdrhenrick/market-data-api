# 1. Escolhemos uma imagem base do Python leve (Slim)
FROM python:3.11-slim

# 2. Definimos a pasta de trabalho dentro do container
WORKDIR /code

# 3. Copiamos o arquivo de dependências para dentro do container
COPY ./requirements.txt /code/requirements.txt

# 4. Instalamos as dependências (sem cache para ficar leve)
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 5. Copiamos o resto do código da pasta 'app'
COPY ./app /code/app

# 6. Comando para rodar a API quando o container iniciar
# --host 0.0.0.0 libera o acesso externo ao container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]