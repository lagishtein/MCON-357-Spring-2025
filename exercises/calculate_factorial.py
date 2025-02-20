import sys
#process input- return a tuple-value, and error message
def process_input(input):
    error_message = None
    value = None
    try:
        value= int (str(input))

        if value <0:
            return None, "Number must be positive!"

        if value >= sys.getrecursionlimit():
            return None, "Number exceeded the recursion limit!"
        return value, error_message
    except ValueError:
        return None, "Number must be an integer!"


# implement factorial_recursive method
def factorial_recursive(number):
    if number == 1 or number == 0:  
        return 1
    else:
        return number * factorial_recursive(number - 1) 



def main():
    print("Factorial Computation Using Recursion")

    #while loop to validate input until correct
    while True:
        number = input("Enter a non-negative integer: ")

     # get the value or error message
        value, error_message = process_input(number)

        if error_message:
            print(error_message)
        else:
            #Call factorial_recursive method
            result = factorial_recursive(int(value))
            print(f"Factorial of {number} is: {result}")
            break

if __name__ == "__main__":
    main()