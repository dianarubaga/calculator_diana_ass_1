# Python Calculator

This project is a simple calculator with six main operations, as seen bellow:

1. Add
2. Subtract
3. Multiply
4. Divide
5. Percentage change
6. Compound growth

Once launched in the terminal the user will be prompted to choose between the operations by choosing a number between 1 to 6. Then the program will ask the user to enter the requested values for each operation and
 print the results.

## Project structure

```text
src/
├── calculator.py       # Reusable calculator functions and terminal window
└── test_calculator.py  # Assertions and boundary-case tests
```

## How to run the calculator

From the project folder, activate the virtual environment:

```bash
source .venv/bin/activate
```
Then start the terminal interface:

```bash
python src/calculator.py
```

## Import the functions

The calculation functions are in `src/calculator.py` and can be imported
into another Python file:

```python
from src.calculator import add, compound_growth

print(add(2, 3))
print(compound_growth(100, 0.05, 2))
```

## Rules and errors

- Division by zero raises `ValueError`.
- Percentage change uses
  `((new_value - original_value) / original_value) * 100`.
- Percentage change raises `ValueError` when `original_value` is zero,
  because zero cannot be used as the percentage-change base.
- Compound growth uses
  `initial_value * (1 + rate) ** periods`.
- Negative compound-growth rates are allowed when `rate > -1`.
- A compound-growth rate of `-1` or lower raises `ValueError`.
- Zero periods return the initial value.
- Negative periods raise `ValueError`.

## Run the tests given 

```bash
python -m tests.test_calculator
```

## Final thoughts of this assignemnt 
As someone with more of a computer science background, it was nice to go back to the roots of programming a bit. It made me pay attention to things we do not usually focus on, which I found really useful. Overall, I thought it was a very nice exercise.