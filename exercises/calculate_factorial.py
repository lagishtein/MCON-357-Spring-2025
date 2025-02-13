# implement factorial_recursive method
def factorial_recursive(number):
    if number in [0, 1]:
        return 1
    else:
        return number*factorial_recursive(number-1)

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
        # Call factorial_recursive method
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
