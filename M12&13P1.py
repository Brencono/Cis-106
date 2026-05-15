name = ("Aaron", "Bob", "Charlie", "Drake", "Emily", "Fran", "George", "Han", "Igor", "Jason")



def display_names(names):
    print("Names in normal order:")
    for names in name:
        print(names)

# Function to display names in reverse order
def display_reverse(names):
    print("\nNames in reverse order:")
    for names in reversed(name):
        print(names)

display_names(name)
display_reverse(name)


