# Import the random module
import random

# Takes student's class name from user
class_name = input("Enter your class name: ")

# Generate random number
random_number = random.randint(1,34)

# Display class information
print()
print("Class Name:", class_name)
print("Selected Student Number:", random_number)