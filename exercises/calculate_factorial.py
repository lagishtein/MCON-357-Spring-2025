# implement factorial_recursive method
from warnings import catch_warnings


def factorial_recursive(number):
    if number == 1 or number == 0:
        return 1
    return number * factorial_recursive(number - 1)


def main():
    try:
        print("Factorial Computation Using Recursion")
        number = int(input("Enter a non-negative integer: "))

        # handle negative input
        while number < 0:
            number = int(input("Must enter a non-negative integer. Please re-enter: "))

        # Call factorial_recursive method
        factorial = factorial_recursive(number)
        print("The factorial of " + str(number) + " is: " + str(factorial))
    except ValueError:
        print("Invalid input. Non integer value entered.")

if __name__ == "__main__":
    main()
