# Getting user input (always returns a string)
student_name = input("FLORINA: ")
student_age = input("18: ")
course_code = input("MC2515: ")

#convert age to an integer
student_age = int(student_age)

#Display the student information
print()
print("name:", student_name)
print("age:", student_age)
print("Course code:", course_code)

#Display the data types
print()
print( "type of name:", type(student_name))
print("type of age:", type(student_age))
print("type of course code:", type(course_code))