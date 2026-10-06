# Simple calculator methods 

def add(a: float, b: float) -> float:
    """ Adding two numbers
    Args:
        a: The first number
        b: The second number
    Returns:
        The sum of a and b
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """Subtracting the second number from the first number
    Args:
        a: The number to subtract from
        b: The number to subtract
    Returns:
        The difference between a and b
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiply two numbers
    Args:
        a: The first number
        b: The second number
    Returns:
        The product of a and b
    """
    return a * b


def divide(a: float, b: float) -> float:
    """Divide the first number by the second number
    Args:
        a: The number to divide
        b: The divisor
    Returns:
        The quotient of a and b
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def percentage_change(original_value: float, new_value: float) -> float:
    """Calculate the percentage change from an original value to a new values
    Args:
        original_value: The starting value
        new_value: The ending value
    Returns:
        The percentage change
    Raises:
        ValueError: If original_value is zero, because percentage change
            cannot use zero as its base value
    """
    if original_value == 0:
        raise ValueError("Original value cannot be zero.")
    return ((new_value - original_value) / original_value) * 100


def compound_growth(
    initial_value: float, rate: float, periods: int
) -> float:
    """Calculate a final value using compound growth
    Args:
        initial_value: The value at the beginning
        rate: The growth rate per period, written as a decimal (positive or negative)
        periods: The number of periods
    Returns:
        The final value after compound growth
    Raises:
        ValueError: If rate is less than or equal to -1, or if periods is
            negative
    """
    if rate <= -1:
        raise ValueError("Rate must be greater than -1.")
    if periods < 0:
        raise ValueError("Periods cannot be negative.")
    return initial_value * (1 + rate) ** periods



def main():
    """Run the calculator menu in the terminal."""
    print("Calculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Percentage Change")
    print("6. Compound Growth")

    choice = input("Choose an operation (1-6):")

    try:
        if choice in {"1", "2", "3", "4"}:
            first_number = float(input("Enter the first number: "))
            second_number = float(input("Enter the second number: "))

            if choice == "1":
                result = add(first_number, second_number)
            elif choice == "2":
                result = subtract(first_number, second_number)
            elif choice == "3":
                result = multiply(first_number, second_number)
            else:
                result = divide(first_number, second_number)
        elif choice == "5":
            original_value = float(input("Enter the original value: "))
            new_value = float(input("Enter the new value: "))
            result = percentage_change(original_value, new_value)
        elif choice == "6":
            initial_value = float(input("Enter the initial value: "))
            rate = float(input("Enter the growth rate as a decimal: "))
            periods = int(input("Enter the number of periods: "))
            result = compound_growth(initial_value, rate, periods)
        else:
            print("Invalid choice. Please choose a number from 1 to 6. byebye")
            return
        
        print(f"Result: {result}") 

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
