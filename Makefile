VENV = .venv
PYTHON = $(VENV)/bin/python
RUN = poetry run
ENV_FILE = .env

help:
	@echo "Usage: make [help|install|run|lint|format|scrape|seed|deploy|clean]"
	@echo "    help"
	@echo "        Display this help message."
	@echo "    install"
	@echo "        install packages."
	@echo "    run"
	@echo "        Run the development server."
	@echo "    lint"
	@echo "        Check style with flake8."
	@echo "    format"
	@echo "        Format the code with black."
	@echo "    scrape"
	@echo "        Scrape dominion card data from the web."
	@echo "    seed"
	@echo "        Seed the database with dominion card data."
	@echo "    deploy"
	@echo "        Deploy the api to Render.com. RENDER_DEPLOY_KEY and RENDER_SERVICE_ID environment variables are required."
	@echo "    clean"
	@echo "        Remove the virtual environment, python caches, and card data."


.PHONY: install
install: pyproject.toml
	POETRY_VIRTUALENVS_IN_PROJECT=true poetry install
	@echo "To activate the virtual environment, run 'poetry shell'"

.PHONY: run
run:
	$(RUN) uvicorn main:app --reload

.PHONY: lint
lint:
	$(RUN) flake8 .

.PHONY: format
format:
	$(RUN) black .

.PHONY: scrape
scrape:
	mkdir -p data
	$(PYTHON) scrape_data.py

.PHONY: seed
seed:
	mkdir -p images
	$(PYTHON) seed_db.py
	rm -rf images

REQUIREMENTS_FILE = requirements.txt

.PHONY: deploy
deploy:
	poetry export --without-hashes --without-urls --output=$(REQUIREMENTS_FILE)
	deta update --env $(ENV_FILE)
	deta deploy
	rm $(REQUIREMENTS_FILE)

.PHONY: clean
clean:
	rm -rf $(VENV) $(DATA_PATH) dominion.db
	find . -type d -name  "__pycache__" -exec rm -r {} +
	@echo "to exit the virtual environment, run 'deactivate'"
