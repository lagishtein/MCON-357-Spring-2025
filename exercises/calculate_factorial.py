# implement factorial_recursive method
def factorial_recursive(number):
     if number == 0:   # base case
            return 1
     else:
            return number * factorial_recursive(number - 1)


def main():
    print("Factorial Computation Using Recursion")

    while True:
        try:
            number = int(input("Enter a non-negative integer: "))

            # handle negative input
            if number < 0:
                print("Invalid input. Please enter a non-negative integer:")
            else:
                break

        except ValueError:
                    print("Invalid input. Please enter an integer.")

    # Call factorial_recursive method
    result = factorial_recursive(number)
    print(f"The factorial of {number} is {result}")

if __name__ == "__main__":
    main()
