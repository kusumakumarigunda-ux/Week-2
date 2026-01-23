# function to calclutate grade and message
def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent work!"
    elif marks >= 80:
        return "B", "Very Good! keep it up!"
    elif marks >= 70:
        return "C", "Good job! you can do even better!"
    elif marks >= 60:
        return "D", "You Passed! work harder!"
    else:
        return "F", "Don't give up! try again!"

# Main program
print("STUDENT GRADE CALCULATOR")
student_name = input("Enter student name:")
# Input validations using while loop
while True:
    try:
        marks =  int(input("enter marks (0-100):"))
        if 0 <= 100:
            break
        else:
            print(" Marks must be in between 0 and 100. Try again.")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

# Function call
grade, message = calculate_grade(marks)

# Display results
print("/n Result for", student_name.upper())
print("Marks:", marks, "/100")
print("Grade:", grade)
print("Message:", message)
