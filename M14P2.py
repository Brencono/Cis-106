class Student:

    def __init__(self, first_name, last_name, district_code, credits):

        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code
        self.credits = credits

    # Method to compute tuition
    def compute_tuition(self):

        # In district
        if self.district_code.upper() == "I":
            tuition = self.credits * 250.00

        # Out of district
        elif self.district_code.upper() == "X":
            tuition = self.credits * 800.00
        
        elif self.district_code.upper() == "G":
            tuition = self.credits * 250.00
        
        else:
            tuition = self.credits * 500.00
        

        return tuition

# Main Program
# Instantiate objects


student1 = Student("John", "Smith", "I", 12)

student2 = Student("Mary", "Jones", "O", 15)

student3 = Student("Day", "Joe", "X", 12)

student4 = Student("Racine", "Jones", "G", 15)






# Display student information
print("STUDENT INFORMATION")
print("--------------------------------------------")

print("Name:", student1.first_name, student1.last_name)
print("District Code:", student1.district_code)
print("Credits:", student1.credits)
print("Tuition Owed: $", student1.compute_tuition())

print("--------------------------------------------")

print("Name:", student2.first_name, student2.last_name)
print("District Code:", student2.district_code)
print("Credits:", student2.credits)
print("Tuition Owed: $", student2.compute_tuition())

print("--------------------------------------------")

print("Name:", student3.first_name, student3.last_name)
print("District Code:", student3.district_code)
print("Credits:", student1.credits)
print("Tuition Owed: $", student3.compute_tuition())

print("--------------------------------------------")

print("Name:", student4.first_name, student4.last_name)
print("District Code:", student4.district_code)
print("Credits:", student2.credits)
print("Tuition Owed: $", student4.compute_tuition())