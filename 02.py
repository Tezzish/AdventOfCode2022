def score(input):
    if(input[0] == "A"):
        if(input[1] == "X"):
            return 3
        elif(input[1] == "Y"):
            return 6
        else:
            return 0
    elif(input[0] == "B"):
        if(input[1] == "X"):
            return 0
        elif(input[1] == "Y"):
            return 3
        else:
            return 6
    else:
        if(input[1] == "X"):
            return 6
        elif(input[1] == "Y"):
            return 0
        else:
            return 3

#item to use against opponent
def item(input):
    if(input[0] == "A"):
        if(input[1] == "X"):
            return 3
        elif(input[1] == "Y"):
            return 1
        else:
            return 2
    elif(input[0] == "B"):
        if(input[1] == "X"):
            return 1
        elif(input[1] == "Y"):
            return 2
        else:
            return 3
    else:
        if(input[1] == "X"):
            return 2
        elif(input[1] == "Y"):
            return 3
        else:
            return 1

f = open("02.txt","r")
lines = f.readlines()
sum = 0
lines.remove("\n")
for i in lines:
    a = i.split(" ")
    a[1] = a[1].strip("\n")
    sum += item(a)
    if(a[1] == "X"):
        sum += 0
    elif(a[1] == "Y"):
        sum += 3
    else:
        sum += 6
print(sum)
