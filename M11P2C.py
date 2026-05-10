# Function to calculate average and total points
def calculate_scores(exam_1,exam_2,exam_3):

    # Compute avg score
    avg_score = (exam_1 + exam_2 + exam_3)/3

    # Compute total points
    total_points = exam_1 + exam_2 + exam_3

    # Return both values
    return avg_score, total_points


# Main program
last_name = (input("Enter Last Name:"))
exam_1 = float(input("Enter first exam score:"))
exam_2 = float(input("Enter second exam score:"))
exam_3 = float(input("Enter third exam score:"))

# Call function
total, avg = calculate_scores(exam_1,exam_2,exam_3)

# Display results
print(f"Students Last Name: {last_name}")
print(f"Total Points: {total}")
print(f"Average Score: {avg}")