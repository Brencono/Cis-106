def batting_avg(hits, attempts):
    if attempts == 0:
        return 0
    return hits / attempts


total_batters = 0

print("Enter players last name")
print("Enter your hits and attempts")
print("Type 'stop' to end the program.\n")

while True:
    last_name = input("Enter the last name or 'stop' to quit: ")

    if last_name.lower() == "stop":
        break

    hits = int(input("How many hits? "))
    attempts = int(input("How many attempts? "))

    # Store the returned batting average
    average = batting_avg(hits, attempts)

    print(f"\nPlayer: {last_name}")
    print(f"Batting Average: {average:.3f}\n")

    total_batters += 1

print(f"Total Batters: {total_batters}")