#!/bin/bash
set -e

source venv/bin/activate;
cd tests;
coverage run --source /Tests/pizza_exercise_docker/code_folder -m pytest --html=pytest_report.html --self-contained-html /Tests/pizza_exercise_docker/tests  || true;
coverage report;
coverage html;
mkdir -p results
rm -rf results/*
mv htmlcov results/.
mv pytest_report.html results/.
mv .coverage results/.
cd results
coverage-badge -o coverage.svg -f
