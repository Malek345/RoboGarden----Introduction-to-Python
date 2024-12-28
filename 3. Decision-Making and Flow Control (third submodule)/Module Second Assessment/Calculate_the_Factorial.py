######   Calculate the Factorial   ######

number = int(input("Enter the number you want to generate factorial: "))

factorial = 1 

# Check for valid input
if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, number + 1):
        factorial *= i  
    # Print the factorial
    print(f"The factorial of {number} is: {factorial}") 
