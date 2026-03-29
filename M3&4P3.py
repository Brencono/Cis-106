last_name = input("Enter your last name")
midterm = input("Enter your midterm score")
final = input("Enter you final exam score")
total_score = float(midterm) * .4 + float(final) *.6
print(str(last_name) + "'s total final score is " + str(total_score))
