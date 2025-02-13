# implement factorial_recursive method
def factorial_recursive(number):
    if n == 1 or n == 0:  
        return 1
    else:
        return n * factorial_recursive(n - 1) 


def main():
    print("Factorial Computation Using Recursion")
    number = int(input("Enter a non-negative integer: "))

    # handle negative input
while number < 0:
    number = int(input("Please enter a non-negative number: "))

    # Call factorial_recursive method
result = factorial_recursive(number)  
print(f"Factorial of {number} is: {result}")

if __name__ == "__main__":
    main()










