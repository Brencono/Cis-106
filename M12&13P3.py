def display_score (last_name, score):
    l = len(last_name)
    for x in range (0,l,1):
        print(x,"",last_name[x],"",score[x])
        
def hilow(last_name, score):

    l = len(last_name)

    hiscore = -1.0
    lowscore = 99999.99

    for y in range(l):

        if score[y] > hiscore:
            hiindex = y
            hiscore = score[y]

        if score[y] < lowscore:
            loindex = y
            lowscore = score[y]

    print("Highest salary:", last_name[hiindex], score[hiindex])
    print("Lowest salary:", last_name[loindex], score[loindex])
            
                            
                            

#opening file
f = open("students.txt", "r")

last_name = []
score = []

lastn = f.readline()

while lastn != "":
    last_name.append(str(lastn).rstrip("\n"))
    s = float(f.readline())
    score.append(s)
    lastn = f.readline()
f.close()

display_score (last_name, score)
hilow(last_name, score)
