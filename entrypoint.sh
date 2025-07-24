#!/usr/bin/env bash

set -e  # Sai imediatamente se algum comando falhar

echo "Entrypoint iniciado - ambiente: ${ENV}"

# Constrói os nomes das variáveis dinamicamente com base no ambiente
DB_HOST_VAR="${ENV}_POSTGRES_HOST"
DB_PORT_VAR="${ENV}_POSTGRES_PORT"

# Expande os valores das variáveis dinamicamente
DB_HOST="${!DB_HOST_VAR}"
DB_PORT="${!DB_PORT_VAR}"

echo "Aguardando o banco de dados em ${DB_HOST}:${DB_PORT}..."

# Função para checar conexão TCP com o banco (usando nc - netcat)
wait_for_db() {
  retries=20
  until nc -z -w5 "$DB_HOST" "$DB_PORT"; do
    retries=$((retries - 1))
    if [ $retries -le 0 ]; then
      echo "Erro: banco de dados não disponível após várias tentativas."
      exit 1
    fi
    echo "Banco de dados indisponível, tentando novamente em 5 segundos..."
    sleep 5
  done
}

wait_for_db

echo "Banco de dados está disponível."

# Executa as migrations do Django para manter o banco atualizado
echo "Executando migrations do Django..."
poetry run python -m app.manage migrate --noinput

# Criação automática do superuser
echo "Criando superuser padrão (se não existir)..."
poetry run python - <<END
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.core.settings")
django.setup()
from django.contrib.auth import get_user_model

User = get_user_model()

username = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
email = os.getenv("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "admin123")

if not User.objects.filter(username=username).exists():
    print(f"Criando superuser '{username}'")
    User.objects.create_superuser(username=username, email=email, password=password)
else:
    print(f"Superuser '{username}' já existe.")
END

# Coleta arquivos estáticos (se necessário)
echo "Coletando arquivos estáticos..."
poetry run python -m app.manage collectstatic --noinput

# Executa o servidor
echo "Iniciando servidor Gunicorn..."
poetry run gunicorn app.core.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --timeout 120 \
    --log-level ${BASE_LOG_LEVEL:-info} \
    --access-logfile - \
    --error-logfile - 

