# Makefile for the Python To-Do App

# Phony targets are not files. This prevents 'make' from getting
# confused if a file with the same name as a target exists.
.PHONY: install requirements run clean

install: venv\Scripts\activate
	venv\Scripts\python -m pip install -r requirements.txt

venv\Scripts\activate: requirements.txt
	python -m venv venv
	@echo "Virtual environment created. Run 'make install' to install dependencies."

# This is the equivalent of your 'freeze' script
requirements:
	@echo "Freezing dependencies to requirements.txt"
	venv\Scripts\python -m pip freeze > requirements.txt

run:
	uvicorn main:app --reload

clean:
	@echo "Cleaning up Python cache and build artifacts..."
	-del /s /q *.pyc
	-for /d /r . %%d in (__pycache__) do @if exist "%%d" rmdir /s /q "%%d"
