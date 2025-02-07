# implement factorial_recursive method
def factorial_recursive(number):
    if number == 1 or number == 0:
        return 1
    return number * (factorial_recursive(number-1))

def main():
    print("Factorial Computation Using Recursion")
    number = int(input("Enter a non-negative integer: "))

    # handle negative input
    if number < 0:
        number = int(input("Number must be positive. Please re-enter: "))
    # Call factorial_recursive method
    print(f"The factorial of {number} is {factorial_recursive(number)}")

if __name__ == "__main__":
    main()
