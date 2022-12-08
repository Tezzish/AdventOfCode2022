f = open("04.txt","r")
lines = f.readlines()
counter = 0
counter2 = 0
for i in lines:
    input = i.split(",")
    #part 1
    if(int(input[0].split("-")[0]) >= int(input[1].split("-")[0]) and int(input[0].split("-")[1]) <= int(input[1].split("-")[1])):
        counter += 1
    elif(int(input[0].split("-")[0]) <= int(input[1].split("-")[0]) and int(input[0].split("-")[1]) >= int(input[1].split("-")[1])):
        counter += 1
    else:
        pass
    #part 2
    if(int(input[0].split("-")[1]) >= int(input[1].split("-")[0]) and int(input[0].split("-")[0]) <= int(input[1].split("-")[1])):
        counter2 += 1
    elif(int(input[1].split("-")[1]) >= int(input[0].split("-")[0]) and int(input[1].split("-")[0]) <= int(input[0].split("-")[1])):
        counter2 += 1
    else:
        pass

print(counter)
print(counter2)