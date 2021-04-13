install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt &&\
			pip install -r requirements_scikit.txt

install_test:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	pip install -r requirements_scikit.txt
	pip install -r requirements_test.txt

test:
	python -m pytest -vv tests/*.py
	#python -m pytest --nbval notebook.ipynb


lint:
	#hadolint Dockerfile #uncomment to explore linting Dockerfiles
	pylint --disable=R,C,W1203,W0702 app.py

all: install lint test
