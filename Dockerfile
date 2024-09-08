FROM python:3.11

# Define diretório de trabalho

WORKDIR /app




# Copia o arquivo pyproject.toml para o contêiner

COPY pyproject.toml poetry.lock /app/




RUN apt update

RUN apt install -q -y git




RUN pip install poetry




# Copia todo o código fonte para a imagem

COPY . /app




# Instala todas as dependências do Poetry de forma global

#RUN poetry config virtualenvs.create false

RUN poetry install --only main




# Comandos a serem executados no inicio da aplicação

CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]
