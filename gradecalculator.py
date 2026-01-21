def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent"
    elif marks >= 75:
        return "B", "Very Good"
    elif marks >= 60:
        return "C", "Good"
    elif marks >= 40:
        return "D", "Pass"
    else:
        return "F", "Fail"

marks = int(input("Enter marks: "))
grade, message = calculate_grade(marks)

print("Grade:", grade)
print("Message:", message)
