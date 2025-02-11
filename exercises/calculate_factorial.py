# implement factorial_recursive method
def factorial_recursive(number):
    if num == 0 or num == 1:
        return 1
    return num * factorial_recursive(num - 1)    


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
