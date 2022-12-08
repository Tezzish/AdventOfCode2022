f = open("01.txt","r")
lines = f.readlines()
list = []
sum = 0
for i in lines:
    if(i == "\n"):
        list.append(sum)
        sum = 0
    else:
        sum += int(i.strip("\n"))
list.append(sum)
list.sort()
print(list[0])
print(list[len(list)-1])