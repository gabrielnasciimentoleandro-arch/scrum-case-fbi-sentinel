.PHONY: setup build validate test all

setup:
	python -m pip install -r requirements.txt

build:
	python scripts/generate_deliverables.py

validate:
	python scripts/validate_project.py

test:
	python -m unittest discover -s tests -v

all: build validate test
