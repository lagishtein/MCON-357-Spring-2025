# implement factorial_recursive method
def factorial_recursive(number):
    if number in [0, 1]:
        return 1
    else:
        return number*factorial_recursive(number-1)

def main():
    print("Factorial Computation Using Recursion")
    number = int(input("Enter a non-negative integer: "))

    # handle negative input
    while number < 0:
        print("The integer must be non-negative, enter again:")
        number = int(input("Enter a non-negative integer: "))

    # Call factorial_recursive method
    factorial_number = factorial_recursive(number)
    print("The factorial of ", number, " is: ", factorial_number)

if __name__ == "__main__":
    main()
