# implement factorial_recursive method
import sys


def factorial_recursive(number):
    if number in [0, 1]:
        return 1
    else:
        return number*factorial_recursive(number-1)

# factorial iterative method, to calculate factorial iteratively
def factorial_iterative(number):
    result = 1
    # start at 2 because multiplying by 1 is extra
    for i in range(2, number + 1):
        result *= i
    return result

def check_valid_input(input_str):
    try:
        number = int(input_str)

        # handle negative input
        if number < 0:
            print("Invalid input. Must be non-negative.")
            return False
        else:
            return True

    except ValueError:
        print("Invalid input. Must be an integer.")
        return False

def calculate_factorial(input_str):
    valid = check_valid_input(input_str)
    if valid:
        number = int(input_str)

        # Handle recursion limit
        if number >= sys.getrecursionlimit() // 2:
            # If number is too large, call factorial_iterative function instead
            print("Number is too large for recursion, switching to using iterative approach")
            return factorial_iterative(number)
        else:
            # Call factorial_recursive function
            return factorial_recursive(number)
    else:
        return None

def main():
    print("Factorial Computation Using Recursion")

    while True:
        number = input("Enter a non-negative integer: ")
        factorial_number = calculate_factorial(number)
        if factorial_number is not None:
            break
        else:
            print("Please try again.")

    print("The factorial of ", number, " is: ", factorial_number)

if __name__ == "__main__":
    main()
