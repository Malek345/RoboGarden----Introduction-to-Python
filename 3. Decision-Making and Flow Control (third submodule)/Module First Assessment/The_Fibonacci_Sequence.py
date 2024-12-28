######   The Fibonacci Sequence   ######

count = int(input("Enter the number of Fibonacci numbers to generate: "))

a, b = 0, 1

# Check for valid input
if count <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence:")
    for i in range(count):
        print(a) 
        a = b
        b = a + b  
