last_name = input("Enter employee last name: ")
salary = float(input("Enter salary: "))
job_level = int(input("Enter job level: "))
if job_level >= 10:
    bonus_rate = 0.25
elif 5 <= job_level <= 9:
    bonus_rate = 0.20
else:
    bonus_rate = 0.10
bonus = salary * bonus_rate
print("Employee Last Name:", last_name)
print("Bonus Ammount: $", bonus)