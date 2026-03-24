install:
	# Install the package using pip
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	# Format the code using black or autopep8
	black *.py mylib/*.py
lint:
	#flake8 or pylint
	pylint --disable=R,C *.py mylib/*.py
test:
	# Run tests using pytest or unittest
	python -m pytest -vv --cov=mylib test_logic.py
build:
	# Build container
deploy:
	# Deploy 
all: install lint test deploy
	# Run all the above steps in sequence