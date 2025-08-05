# Import math module
import math

# Takes a radius of circle from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate area and circumference
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

# Print result
print()
print("radius:" + str(radius))
print("area:" + str(area))
print("circumference:" + str(circumference))