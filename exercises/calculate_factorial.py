# implement factorial_recursive method
def factorial_recursive(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial_recursive(number - 1)    
5


def main():
    print("Factorial Computation Using Recursion")
    while True:
        try:
            number = int(input("Enter a non-negative integer: "))

             # handle negative input
            if number< 0:
                 raise ValueError("This number is negative")
            break
        except ValueError as e:
            print(e)

    # Call factorial_recursive method
    result = factorial_recursive(number)

    # Print the result
    print(f"The factorial of {number} is {result}.")


if __name__ == "__main__":
    main()
