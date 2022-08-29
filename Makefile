VENV = .venv
PYTHON = $(VENV)/bin/python

.PHONY: all
all: install seed

help:
	@echo "Usage: make [help|install|run|lint|format|scrape|seed|clean]"
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
	@echo "    clean"
	@echo "        Remove the virtual environment, python caches, and card data."


.PHONY: install
install: $(VENV)/bin/activate

$(VENV)/bin/activate: pyproject.toml
	POETRY_VIRTUALENVS_IN_PROJECT=true poetry install
	@echo "To activate the virtual environment, run 'source $(VENV)/bin/activate'"

.PHONY: run
run: $(VENV)/bin/activate
	$(VENV)/bin/uvicorn app.main:app --reload

.PHONY: lint
lint: $(VENV)/bin/activate
	$(VENV)/bin/flake8 .

.PHONY: format
format: $(VENV)/bin/activate
	$(VENV)/bin/black .

.PHONY: scrape
scrape: $(VENV)/bin/activate
	mkdir -p data
	$(PYTHON) scrape_data.py

.PHONY: seed
seed: $(VENV)/bin/activate
	$(PYTHON) seed_db.py

.PHONY: clean
clean:
	rm -rf $(VENV) $(DATA_PATH) dominion.db
	find . -type d -name  "__pycache__" -exec rm -r {} +
	@echo "to exit the virtual environment, run 'deactivate'"
