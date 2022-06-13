VENV = .venv

.PHONY: install
install: $(VENV)/bin/activate

$(VENV)/bin/activate: pyproject.toml
	export POETRY_VIRTUALENVS_IN_PROJECT=true
	poetry install

.PHONY: run
run: $(VENV)/bin/activate
	$(VENV)/bin/uvicorn app.main:app --reload

.PHONY: lint
lint: $(VENV)/bin/activate
	$(VENV)/bin/flake8 app

.PHONY: format
format: $(VENV)/bin/activate
	$(VENV)/bin/black app

.PHONY: clean
clean:
	rm -rf $(VENV)
	find . -type d -name  "__pycache__" -exec rm -r {} +
