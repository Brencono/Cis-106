total_students_input = 0
message = "Do you want to run this program Yes or No."
choice =""
while choice != 'No':
    last_name = input('Whats you last name?')
    first_score = float(input('Whats your first exam score?'))
    second_score = float(input('Whats your second exam score?'))
    avg_score = (first_score + second_score)/2
    print('Last name of student:', last_name, 'Average score:',avg_score)
    choice = input(message)
    print(choice)
    total_students_input += 1
print('Total students that entered data is',total_students_input)