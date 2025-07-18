.PHONY: install makemigrations migrate createsuperuser run-server update

install:
	@echo "Instalando dependências do projeto..."
	poetry install --no-root

makemigrations:
	@echo "Gerando novas migrações a partir dos modelos..."
	poetry run python -m app.manage makemigrations

migrate: makemigrations
	@echo "Aplicando migrações ao banco de dados..."
	poetry run python -m app.manage migrate

createsuperuser:
	@echo "Criando usuário administrador..."
	poetry run python -m app.manage createsuperuser

run-server:
	@echo "Iniciando o servidor de desenvolvimento..."
	poetry run python -m app.manage runserver

update: install migrate
	@echo "Ambiente atualizado com dependências e migrações aplicadas."
