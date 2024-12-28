
import math  # Importing math module for the constant pi

# Input the radius from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate the circumference and area
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Print the results
print(f"The circumference of the circle is: {circumference}")
print(f"The area of the circle is: {area}")