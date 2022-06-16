VENV = .venv

.PHONY: install
install: $(VENV)/bin/activate

$(VENV)/bin/activate: pyproject.toml
	POETRY_VIRTUALENVS_IN_PROJECT=true poetry install
	poetry shell

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
	$(VENV)/bin/python scrape_data.py

.PHONY: seed
seed: $(VENV)/bin/activate
	$(VENV)/bin/python seed_db.py

.PHONY: clean
clean:
	rm -rf $(VENV)
	find . -type d -name  "__pycache__" -exec rm -r {} +
