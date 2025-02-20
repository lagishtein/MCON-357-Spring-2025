#NechamaBookson
def factorial_recursive(number):
    validate_method_input(number)  # Ensure valid input before recursion
    if number == 1 or number == 0:
        return 1
    return number * factorial_recursive(number - 1)

def factorial_iterative(number):
    validate_method_input(number)  # Ensure valid input before iteration
    result = 1
    while number > 1:
        result *= number
        number -= 1
    return result

def validate_method_input(number):
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a non-negative integer")

def main():
    print("Factorial Computation Using Recursion")
    string = input("Enter a non-negative integer: ")

    number, message = process_input(string)

    if message:  # If there's an error message, display it and exit
        print(message)
        return

    print_factorial(number)

def print_factorial(number):
    print(f"The factorial of {number} is {factorial_recursive(number)}")

def process_input(input_str):
    try:
        value = int(input_str)
        if value < 0:
            return None, 'Error: Number cannot be negative'
        return value, ''
    except ValueError:
        return None, "Error: Input must be a non-negative integer"

if __name__ == "__main__":
    main()