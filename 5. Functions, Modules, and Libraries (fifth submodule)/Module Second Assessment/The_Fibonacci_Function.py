def fibonacci(n):

    # Base conditions
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive return: Sum of the two preceding Fibonacci numbers
    return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter the position of the Fibonacci number to calculate: "))
result = fibonacci(num)
print(f"The {num}th Fibonacci number is: {result}")