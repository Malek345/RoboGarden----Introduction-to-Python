def factorial(n):

    # Base condition: Factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    
    # Recursive return: Multiply n by the factorial of (n-1)
    return n * factorial(n - 1)

num = int(input("Enter a number to calculate its factorial: "))
result = factorial(num)
print(f"The factorial of {num} is: {result}")