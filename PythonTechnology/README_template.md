## Python Technology 101<br>

## Table of content

#### [Code formatters](#code-formatters)

- [Black](#--black)
- [isort](#--isort)

#### [Code checkers](#code-checkers)

- [Flake8](#--flake8)
- [Bandit](#--bandit)
- [Safety](#--safety)
- [MyPy](#--mypy)

#### [Tests](#tests)

- [PyTest](#--pytest)
- [UnitTest](#--unittest)
- [Coverage](#--coverage)

#### [Deployment environment](#deployment-environment)

- [Docker](#--docker)
- [Docker-Compose](#--docker-compose)
- [Kubernetes](#--kubernetes)

#### [Development tools](#development-tools)

- [Pycharm](#--pycharm)
- [vscode](#--vscode)
- [Kubernetes](#--kubernetes)

#### [Every project MUST HAVE](#every-project-must-have)

- [README.md](#--readmemd)
- [requirements.txt](#--requirementstxt)

#### [Modules&Packages](#modulespackages)

- [pip3](#--pip3)
- [venv](#--venv)
- [PyPI](#--pypi)

## Code formatters:

#### - Black - `Uncompromising code formatter`

#### - isort - `Import sorting tool in alphabetical order`

## Code checkers:

#### - Flake8 - `Code linter and code smells finder`

#### - Bandit - `Looking for left AWS keys etc.`

#### - Safety - `Checking safety of dependency modules`

#### - MyPy - `Static typing analyzer`

## Tests:

#### - PyTest - `Pythonic tests framework`

#### - UnitTest - `Object Oriented tests framework`

#### - Coverage - `Check tests coverage of your code`

## Deployment environment:

#### - Docker - `Contenerisation tool, removes OS dependencies`

#### - Docker-Compose - `Manager for multiple docker containers - low scale`

#### - Kubernetes - `Containers orchestrator for great scale`

## Development tools:

#### - Pycharm - `Python IDE for python code development by JetBrains`

#### - vscode - `Open source IDE for python and frontend, multiple libraries`

## Every project **MUST HAVE**

#### - README.md - `Project explanation file, contains hot to install and about project`

#### - requirements.txt - `Conventional file for telling everyone about packages in project`

## Modules&Packages

#### - pip3 - `Package to download packages from PyPI repository`

#### - venv - `Virtual Environment so our development won't kill our OS libraries`

#### - PyPI - `Python Package Index, repository for packages to be downloaded`

## Quality Assurance

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

Change directory to Task_2 Run command:

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

