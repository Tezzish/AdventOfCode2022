def priority(i):
    if(i.isupper()):
        return ord(i) - (65-27)
    else:
        return ord(i) - 96

def findPriority(i):
    firstComp, secondComp = i[:(len(i)//2)], i[(len(i)//2):]
    #changes first part into a set
    firstComp = set(firstComp)
    for i in secondComp:
        if(i in firstComp):
            return priority(i)
    return 0

def findItem(a, b, c):
    a = set(a)
    b = set(b)
    for i in c:
        if(i in a and i in b):
            return priority(i)

f = open("03.txt","r")
lines = f.readlines()
lines2 = [[]]
#lines.remove("\n")
total = 0
priorities = 0
counter = 0
miniCounter = 0

for i in lines:
    miniCounter += 1
    total += findPriority(i)
    lines2[counter].append(i)
    if(miniCounter == 3 and counter != 100):
        lines2.append([])
        miniCounter = 0
        counter += 1
for i in lines2:
    if(len(i) == 3):
        priorities += findItem(i[0], i[1], i[2])

print(total)
print(priorities)