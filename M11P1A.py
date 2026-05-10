def calculate_total(quantity, price):
    total = quantity * price
    
    if total > 10000:
        total = total * 0.90
    return total

grand_total = 0

print("Enter quantities and prices.")
print("Type 'stop' as the quantity to end the program.\n")

while True:
    quantity_input = input("Enter quantity (or 'stop' to quit): ")

    if quantity_input.lower() == "stop":
        break

    quantity = float(quantity_input)

    price = float(input("Enter price: "))

    total = calculate_total(quantity, price)

    print(f"Quantity: {quantity}")
    print(f"Price: ${price:.2f}")
    print(f"Total: ${total:.2f}\n")

    grand_total += total

print(f"Total Extended Price: ${grand_total:.2f}")