
input_ = input("Do you want to cehck the highest scores, Yes or No? ") 
if input_ == ("Yes"):
    
    scores = []
    names = []
    result_f = open("results.txt")
    for line in result_f:
        (name, score)= line.split()
        scores.append(float(score))
        names.append(name)
    result_f.close()

    scores.sort()
    scores.reverse()

    names.sort()

    print("The Top 3 Scores Were: ")

    print(names[0], scores[0])
    print(names[1], scores[1])
    print(names[2], scores[2])

    #print("Have a great day!") 

else: 
    print("Have a great day!")

#print("Have a wonderful day!")

    
k = input("Close Tab To Exit")
