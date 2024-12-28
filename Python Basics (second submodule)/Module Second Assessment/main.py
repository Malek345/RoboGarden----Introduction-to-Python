first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

sum_result = first_number + second_number
print(f"Sum: {sum_result}")

subtraction = first_number - second_number
print(f"Subtraction: {subtraction}")

multiplication = first_number * second_number
print(f"Multiplication: {multiplication}")

if second_number != 0:
    division = first_number / second_number
    print(f"Division: {division}")
else:
    division = "Undefined (cannot divide by zero)"

