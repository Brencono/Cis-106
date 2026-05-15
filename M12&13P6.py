
# Function to print dictionary contents
def display_players(players):

    print("PLAYER NAME\tBATTING AVERAGE")
    print("----------------------------------")

    for name, average in players.items():
        print(name, "\t\t", average)


# Create empty dictionary
players = {}

# Open file
f = open("players.txt", "r")

# Read first player name
name = f.readline().rstrip("\n")

# Read until end of file
while name != "":

    average = float(f.readline())

    # Add to dictionary
    players[name] = average

    # Read next player
    name = f.readline().rstrip("\n")

f.close()

display_players(players)