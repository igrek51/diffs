.PHONY: venv

venv:
	python3 -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt -r requirements-dev.txt
	pip install -e .
