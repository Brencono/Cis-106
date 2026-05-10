def calculate_price(msrp, make, model, electric_code):

    if electric_code.upper() == "Y":
        discount_percent = 0.30

    elif make.lower() == "honda" and model.lower() == "accord":
        discount_percent = 0.10

    elif make.lower() == "toyota" and model.lower() == "rav4":
        discount_percent = 0.15

    else:
        discount_percent = 0.05

    discounted_price = msrp * (1 - discount_percent)

    total_price = discounted_price * 1.07

    return total_price


total_msrp = 0
total_sales_price = 0

while True:

    choice = input("Would you like to enter a vehicle? (Yes or No): ")

    if choice.lower() == "no":
        break

    elif choice.lower() == "yes":

        make = input("Enter make: ")
        model = input("Enter model: ")
        electric_code = input("Is it an electric vehicle? (Y or N): ")
        msrp = float(input("Enter MSRP: "))

        sales_price = calculate_price(msrp, make, model, electric_code)

        print("\nVehicle Information")
        print(f"Make: {make}")
        print(f"Model: {model}")
        print(f"MSRP: ${msrp:.2f}")
        print(f"Out-the-Door Price: ${sales_price:.2f}\n")

        total_msrp += msrp
        total_sales_price += sales_price

    else:
        print("Please enter Yes or No.\n")

print("\nFinal Totals")
print(f"Total MSRP: ${total_msrp:.2f}")
print(f"Total Sales Price: ${total_sales_price:.2f}")