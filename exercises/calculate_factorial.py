# implement factorial_recursive method
def factorial_recursive(number):
    if number == 1 or number == 0:
        return 1
    try:
        return number * factorial_recursive(number - 1)
    except RecursionError:
        raise RecursionError(f"Recursion limit exceeded at number {number}. "
                             f"Consider using an iterative approach or increasing the recursion limit.")

def factorial_iterative(number):
    result = 1
    while number > 1:
        result *= number
        number -= 1
    return result

def main():
    print("Factorial Computation Using Recursion")
    string = input("Enter a non-negative integer: ")
    number, message = process_input(string)
    # Call factorial_recursive method
    print_factorial(number)


def print_factorial(number):
    print(f"The factorial of {number} is {factorial_recursive(number)}")


def process_input(input_str):
    error_message = ''
    value = None
    try:
        value = int(input_str)
        if value < 0:
            return None, 'Number cannot be negative'
        return value, error_message
    except ValueError as ex:
        error_message = "Number must be an integer"
        return value, error_message

if __name__ == "__main__":
    main()
