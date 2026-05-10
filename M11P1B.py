def forecast_sales(month, sales):

    month = month.lower()

    if month in ["jan", "feb", "mar"]:
        percent = 0.10
    elif month in ["apr", "may", "jun"]:
        percent = 0.15
    elif month in ["jul", "aug", "sep"]:
        percent = 0.20
    elif month in ["oct", "nov", "dec"]:
        percent = 0.25
    else:
        percent = 0

    next_month_sales = sales * (1 + percent)

    return next_month_sales


while True:

    choice = input("Would you like to do this program (Yes or No): ")

    if choice.lower() == "no":
        break


    last_name = input("Enter last name: ")
    month = input("Enter months first 3 letters (Jan-Dec): ")
    sales = float(input("Enter sales amount: "))

    forecast = forecast_sales(month, sales)

    print(f"\nLast Name: {last_name}")
    print(f"Month: {month}")
    print(f"Current Sales: ${sales:.2f}")
    print(f"Next Month Forecast Sales: ${forecast:.2f}\n")