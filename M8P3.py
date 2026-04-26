total_bonus = 0
input_file = 'input.txt' 
with open (input_file) as input_file: employee_records = input_file.readlines()
clean_employee_records = [employee_record.strip() for employee_record in employee_records]

for clean_employee_records in clean_employee_records:
    split_employee_record = clean_employee_records.split(';')
    # print(split_employee_record)
    name = split_employee_record[0]
    salary = float(split_employee_record[1])
    if salary >= 100000:
        bonus = salary * 0.20
    elif salary >= 50000:
        bonus = salary * 0.15
    else:
        bonus = salary * 0.10
    print('Name:', name, 'Salary:', salary, 'Bonus:', bonus)
    total_bonus += bonus

print('Total Bonus given is', total_bonus)

