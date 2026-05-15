students_grades = {
    "Ana": [90, 85, 88],
    "Bob": [75, 80, 79],
    "Chap": [95, 92, 96],
    "David": [88, 84, 90]
}


# Function to calculate student averages
def calculate_averages(data):

    averages = []

    for name, grades in data.items():

        avg = sum(grades) / len(grades)

        averages.append([name, round(avg, 2)])

    return averages


# Call function
student_averages = calculate_averages(students_grades)


# Print student averages
print("\n")
print("STUDENT GRADE AVERAGES")
print("------------------------------------------------")
print("Student Name\tGrades\t\t\tAverage")
print("------------------------------------------------")

for student in students_grades:

    grades = students_grades[student]

    avg = sum(grades) / len(grades)

    print(student, "\t\t", grades, "\t", round(avg, 2))


# Calculate class average for each grade
grade1_total = 0
grade2_total = 0
grade3_total = 0

count = len(students_grades)

for grades in students_grades.values():

    grade1_total += grades[0]
    grade2_total += grades[1]
    grade3_total += grades[2]

grade1_avg = grade1_total / count
grade2_avg = grade2_total / count
grade3_avg = grade3_total / count


# Print class averages
print("------------------------------------------------")
print("Class Average Grade 1:", round(grade1_avg, 2))
print("Class Average Grade 2:", round(grade2_avg, 2))
print("Class Average Grade 3:", round(grade3_avg, 2))