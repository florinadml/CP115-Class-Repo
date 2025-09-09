# Students Classification System
# Get student information
student_name = input("Enter student name: ")
gpa = float(input("Enter GPA (0.0-4.0): "))
credit_hours = int(input("Enter credit hours: "))

# TODO your code here
if credit_hours >= 12 and gpa >= 3.8 :
   classification = "Dean's List"
elif credit_hours >= 12 and gpa >=3.5 :
   classification =  "Honor Roll"
elif gpa  >= 2.0 :
   classification = "Good Standing"
elif gpa < 2.0:
   classification = "Academic Probation"
else:
   classification = "Part Time Students"

# Display results
print(f"\nStudent: {student_name}")
print(f"GPA: {gpa}")
print(f"Credit Hours: {credit_hours}")
print(f"Classification: {classification}")
