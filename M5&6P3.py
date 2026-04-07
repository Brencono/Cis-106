part_number = input("Please enter your part number")
qty = int(input("Please enter how many items you have"))
if part_number == "10" or part_number == "55":
   unit_price = 1
elif part_number == "99":
    unit_price = 2
elif  part_number == "80" or part_number =="70":
    unit_price = 3
else: 
    unit_price = 5
total = float(qty)*float(unit_price)
print("Part Number: ", part_number)
print("Your unit price is ", unit_price)
print("Your total is ", total)


