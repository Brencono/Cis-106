qty = input("Please enter how many items you have")
if float(qty) >= 1000:
    unitprice =  3
else:
    unitprice = 5
extprice = float(qty)*float(unitprice)
tax = float(extprice) * .07
total = float(extprice) + float(tax)
print("Your quantity for your item is ", float(qty))
print("Your unit price is ", unitprice)
print("your extended price is ", extprice)
print("Your total is ", total)
