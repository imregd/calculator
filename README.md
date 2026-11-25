## Calculator

this is a calculator app that performs arithmetic calculations based on the user's input

It is a Python 3 calculator used from the terminal (CLI), built step by step in SCCM4910

## What it will do
add, subtract, multiply and divide two numbers and then display the result

## How to run it

execute run.sh
enter first number, operator (+ - * /), then second number.
The program prints Result: followed by the answer.


sample test:
6
*
7

this should give 42


## Acceptance Criteria

the batch calculator shall perform arithmetic calculations, specifically: Addition, Subtraction, Multiplication and Division

the batch calculator shall handle non zero inputs

the batch calculator should return suitable error messages

## Prerequisites

Python 3
test dependancy
sccm 4910 environment activation command: 

source /opt/python-venv/sccm-4910/bin/activate
python3 -m pytest --version

ensure it prints out a version

run ./check.sh to have automated tests
