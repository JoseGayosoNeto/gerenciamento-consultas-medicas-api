# Imagem base oficial do Python utilizada
FROM python:3.12-slim

# Define o diretório de trabalho atual
WORKDIR /opt/project

# Definição de algumas variáveis de ambiente
# PYTHONDONTWRITEBYTECODE = Evita a geração de arquivos .pyc no container
# PYTHONBUFFERED = Evita que o Python use buffers nas saídas padrões (stdout) e saídas de erros (stderr),
# garantindo que logs e prints apareçam em em tempo real, sem atrasos
# POETRY_VERSION = Define a versão do Poetry que será instalada no container
# PYTHONPATH = Adiciona o diretório de trabalho atual ao caminho de importações do Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONBUFFERED=1 \
    POETRY_VERSION=2.1.3 \
    PYTHONPATH=.

# Instalação de dependências do sistema
RUN set -xe \
    && apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends build-essential netcat-openbsd curl \
    && pip install poetry==${POETRY_VERSION} \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instalação de dependências do Python
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root

# Copia os arquivos do projeto
COPY README.md Makefile ./
COPY app app

# Expõe a porta do servidor Django
EXPOSE 8000

# Garante que os arquivos de logs, arquivos estáticos e arquivos de mídia existam no container
RUN mkdir -p /opt/project/staticfiles /opt/project/mediafiles /opt/project/logs

# Define o entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
