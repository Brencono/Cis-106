principle_cd = float(input("Please enter the principle"))
mat_cd = float(input("Please enter date of maturity"))
if principle_cd > 100000 and mat_cd == 5:
   int_rate = .06
elif 50000 <= principle_cd <= 100000 and mat_cd == 10:
    int_rate = 0.05
elif 50000 <= principle_cd <= 100000 and mat_cd == 5:
    int_rate = 0.04
else:   
    int_rate = .02
first_int = (principle_cd) * (int_rate)
print("Principle: $", principle_cd)
print("Interest rate: $", int_rate)
print("Interest in 1st year: $", first_int)