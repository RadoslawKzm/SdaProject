#!/bin/bash
set -e

cd /App/tests;
coverage run --source /App/code_folder -m pytest --html=pytest_report.html --self-contained-html /App/tests  || true;
coverage report;
coverage html;
/bin/bash
rm -rf results/*
mv /App/tests/htmlcov /App/tests/results/.
mv /App/tests/pytest_report.html /App/tests/results/.
mv /App/tests/.coverage /App/tests/results/.
cd /App/tests/results/
coverage-badge -o coverage.svg -f
