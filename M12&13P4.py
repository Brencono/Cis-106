# Create dictionary with student names and grades
students = {"Ana":90,"Bob":85,"Chap": 95,"David":88}

# Print table header
print("Student Name\tGrade")

# Variable to store total grades
total = 0

# Print student names and grades
for name, grade in students.items():
    print(name, "\t\t\t", grade)
    total += grade

# Calculate class average
average = total / len(students)

# Print class average
print("-------------------------")
print("Class Average:", round(average, 2))