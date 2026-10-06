"""Assertions for the calculator functions."""

from src.calculator import (
    add,
    compound_growth,
    divide,
    multiply,
    percentage_change,
    subtract,
)


def run_assertions() -> None:
    """Run the required calculator checks and boundary-case checks."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(1.5, 2.5) == 4.0

    assert subtract(10, 4) == 6
    assert subtract(0, 0) == 0
    assert subtract(-3, -2) == -1

    assert multiply(3, 4) == 12
    assert multiply(0, 99) == 0
    assert multiply(2.5, 2) == 5.0

    assert divide(10, 2) == 5
    assert divide(-9, 3) == -3
    assert divide(7.5, 2.5) == 3.0

    try:
        divide(10, 0)
    except ValueError as error:
        assert str(error) == "Cannot divide by zero."
    else:
        raise AssertionError("divide should reject division by zero")

    assert percentage_change(100, 120) == 20
    assert percentage_change(-100, -80) == -20
    assert percentage_change(80, 60) == -25

    try:
        percentage_change(0, 10)
    except ValueError as error:
        assert str(error) == "Original value cannot be zero."
    else:
        raise AssertionError("percentage_change should reject a zero original value")

    assert compound_growth(100, 0.10, 2) == 121.00000000000001
    assert compound_growth(100, -0.10, 1) == 90
    assert compound_growth(100, 0.10, 0) == 100

    for invalid_rate in (-1, -1.5):
        try:
            compound_growth(100, invalid_rate, 2)
        except ValueError as error:
            assert str(error) == "Rate must be greater than -1."
        else:
            raise AssertionError("compound_growth should reject this rate")

    try:
        compound_growth(100, 0.10, -1)
    except ValueError as error:
        assert str(error) == "Periods cannot be negative."
    else:
        raise AssertionError("compound_growth should reject negative periods")


if __name__ == "__main__":
    run_assertions()
    print("All calculator assertions passed.")
