name = ("Aaron", "Bob", "Charlie", "Drake", "Emily", "Fran", "George", "Han", "Igor", "Jason")

test_score = (70, 99, 100, 56, 76, 90, 65, 89, 45, 84)


def display_names(names, test_score):
    print("Students and Exam Scores:")
    for i in range(len(names)):
        print(names[i], "-", test_score[i],"%") 


display_names(name, test_score)
