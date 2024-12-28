def calculate_average(numbers):

    # Check if the list is empty to avoid division by zero
    if len(numbers) == 0:
        return 0
    
    # Get the sum of the list
    total_sum = sum(numbers)
    
    # Divide it by its length to get the average
    average = total_sum / len(numbers)
    
    return average

# Example list of numbers
numbers = [10, 20, 30, 40, 50]

# Calculate the average
result = calculate_average(numbers)

# Print the result
print(f"The average of the list is: {result}")
