##Task_2<br>


[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Code style: black](https://img.shields.io/badge/code%20style-Flake8-green)](https://github.com/PyCQA/flake8)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![security: bandit](https://img.shields.io/badge/security-safety-yellow)](https://github.com/pyupio/safety)
[![](tests/results/coverage.svg)]()

<br>coverage badge will appear after running tests :)<br>
####Time for task: 3 days
- If I can do it in 3 days, think what I can do in one sprint :D


## Table of content

 - [Technology stack](#technology stack)
 - [Quality Assurance](#quality assurance)
 - [Installation](#installation)
 - [Running the service](#running the service)
 - [Tests](#tests)
 - [Before commit](#before commit)

##Technology Stack

 - Python 3.6
 - FastAPI 0.68.1
 - uvicorn 0.15.0
 - coverage 5.5
 - pytest 6.2.4

##Quality Assurance
##### Swagger documentation:
 - http://127.0.0.1:8000/docs
 - http://localhost:8000/docs

##### Clean Code:
 - Black: uncompromising static code formatter
 - Flake8: python3 linter
 - isort: import sorting
 - Pre-commit: hooks for big files etc.

##### Security :
 - bandit: any left credential or AWS key
 - safety: any known package vulnerability

##### Tests:
 - coverage.py: measuring test coverage of application
 - pytest: testing framework



## Installation
 - Docker Desktop Latest (Windows)
 - Docker (Linux)
 - remember to run docker deamon/desktop to avoid errors ;)

## Running the service

##### Docker start & build
Change directory to Task_2
Run command:
```
$ docker-compose build base && docker-compose up --build task2-app && docker-compose rm -fsv
```

##### Close docker
CTRL+C in command line to keyboard interrupt or:
```
$ docker-compose down
```


## Tests
Begin in main folder
```
$ docker-compose build base && docker-compose up --build task2-tests && docker-compose rm -fsv
```
Open results html file in browser:<br>
Coverage results: ./Task_2/tests/results/htmlcov/index.html<br>
Pytest results: ./Task_2/tests/results/pytest_results.html<br>


## Before commit
Steps to take before commit or your commit will not be accepted.<br>
In future I would do full CI/CD process verifying code quality.<br>


Before you send the code to the server, please runt this tests
```
/Task_2$ python -m black --check -l 120 --exclude=venv .
/Task_2$ python -m flake8 . --ignore E501
/Task_2$ python -m isort --check-only --diff .
/Task_2$ python -m mypy --html-report ./tests/results/mypy .
/Task_2$ bandit ./code_folder -r
/Task_2$ safety check --full-report
```
Part of errors you can fix running:
```
/Task_2$ python -m black -l 120 --exclude=venv .
/Task_2$ python -m isort .
```
