.PHONY: install makemigrations migrate createsuperuser run-server update install-pre-commit-hooks lint

install:
	@echo "Instalando dependências do projeto..."
	poetry install --no-root

install-pre-commit-hooks:
	@echo "Instalando hooks do pre-commit do projeto..."
	poetry run pre-commit uninstall
	poetry run pre-commit install

# Exige que os hooks do pre-commit estejam instalados anteriormente
lint:
	@echo "Realizando verificação do código-fonte..."
	poetry run pre-commit run --all-files

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

update: install install-pre-commit-hooks migrate
	@echo "Ambiente atualizado com dependências e migrações aplicadas."
