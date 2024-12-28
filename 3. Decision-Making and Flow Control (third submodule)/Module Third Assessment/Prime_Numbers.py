######   Prime Numbers   ######

limit = int(input("Enter the upper limit to find prime numbers: "))

print(f"Prime numbers up to {limit}:")

# Loop through each number from 2 to the user-specified limit
for num in range(2, limit + 1):  # Start from 2 (smallest prime number)
    is_prime = True  
    for i in range(2, int(num ** 0.5) + 1):  # Check divisors up to the square root of the number
        if num % i == 0:  
            is_prime = False
            break
    if is_prime:
        print(num)  
