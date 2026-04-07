qtyw = input("Please enter how many widgets you have")
if float(qtyw) > 10000:
   unitprice =  10
else:float(qtyw) > 5000
unitprice = 20
if float(qtyw) < 5000:
    unitprice = 20
extprice = float(qtyw)*float(unitprice)
tax = float(extprice) * .07
total = float(extprice) + float(tax)
print("your extended price is ", extprice)
print("Your tax ammount is ", tax)
print("Your unit price is ", unitprice)
print("Your total is ", total)

