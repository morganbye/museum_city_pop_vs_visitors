SHELL:=/bin/bash

.PHONY: setup

venv_path = .venv

format:
	black src/

build:
	@source $(venv_path)/bin/activate && \
	docker-compose build

run:
	@source $(venv_path)/bin/activate && \
	docker-compose up

test:
	@source $(venv_path)/bin/activate && \
	pytest --cov=src

ensure-venv:
	@if [[ ! -d "$(venv_path)" || ! -f "$(venv_path)/bin/activate" ]]; then \
		PIPENV_VENV_IN_PROJECT=true \
		pipenv --python 3.7 \
	; fi
