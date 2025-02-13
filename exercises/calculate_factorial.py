# implement factorial_recursive method
def factorial_recursive(number):
    if number in [0, 1]:
        return 1
    else:
        return number*factorial_recursive(number-1)

def main():
    print("Factorial Computation Using Recursion")

    while True:
        number_input = input("Enter a non-negative integer: ")

        try:
            number = int(number_input)

            # handle negative input
            if number < 0:
                print("Invalid input. Must be non-negative.")
            else:
                break # If valid input, exit the loop

        except ValueError:
            print("Invalid input. Enter a valid integer.")

    # Call factorial_recursive method
    factorial_number = factorial_recursive(number)
    print("The factorial of ", number, " is: ", factorial_number)

if __name__ == "__main__":
    main()
