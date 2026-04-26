total_tuition = 0
total_students = 0

students_file = 'students.txt' 
with open (students_file) as students_file: students_records = students_file.readlines()
clean_students_records = [students_record.strip() for students_record in students_records]
# print(clean_item_records)

for clean_students_records in clean_students_records:
        split_students_record = clean_students_records.split(';')
        student_name = split_students_record[0]
        if split_students_record[1] == 'I':
            cost = 250
        else: 
            cost = 500
        credits_taken = float(split_students_record[2])
        tuition = credits_taken * cost
        # print(tuition)
        print('Students Name:',student_name,'|Credits take:',credits_taken,'|Tuition:$',tuition)
        total_tuition += tuition
        total_students += 1

print('Total tuition is', total_tuition,'and total number of students is',total_students)
        
        