tickets = int(input("Enter number of concert tickets: "))
if tickets >= 25:
    price = 50
elif 10 <= tickets <= 24:
    price = 60
elif 5 <= tickets <= 9:
    price = 70
else:
    price = 75
total_cost = tickets * price
print("Number of Tickets", tickets)
print("Price per Ticket $",price)
print("Total Cost $", total_cost)
