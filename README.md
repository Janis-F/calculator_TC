# Calculator

Calculator is a Python library for making simple mathematical computations. 

## Description

Calculator can perform the following operations:
1) Addition;
2) Subtraction;
3) Multiplication;
4) Division;
5) Take root of number;
6) Keep track of internal memory and reset it.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install calculator.

```bash
pip install git+https://github.com/Janis-F/calculator
```

## Usage

```python
from calculator.calculator import Calculator
calculator = Calculator()

# returns memory
calculator.memory()

# resets memory
calculator.reset_memory()

# perform operations with memory 
calculator.addition(0)
calculator.subtraction(0)
calculator.multiply(0)
calculator.division(0)
calculator.root(2)
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
