# Function to calculate discount amount and discounted price
def calculate_discount(quantity, price, discount_rate):

    # Compute total price
    total = quantity * price

    # Compute discount amount
    discount_amount = total * discount_rate

    # Compute discounted price
    discounted_price = total - discount_amount

    # Return both values
    return discount_amount, discounted_price


# Main program
quantity = int(input("Enter quantity: "))
price = float(input("Enter price: "))
discount_rate = float(input("Enter discount rate (decimal form): "))

# Call function
discount, final_price = calculate_discount(quantity, price, discount_rate)

# Display results
print("\nResults")
print(f"Quantity: {quantity}")
print(f"Price: ${price:.2f}")
print(f"Discount Amount: ${discount:.2f}")
print(f"Discounted Price: ${final_price:.2f}")

