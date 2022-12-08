from collections import deque
f = open("051.txt", "r")
f2 = open("052.txt", "r")
l = f.readlines()
l2 = f2.readlines()
stacks = []
queues = []

for i in range(9):
    stacks.append(deque())
    queues.append(list())

for i in range(len(l) - 1):
    #the length of l - 1 is because the last line is empty
    line = l[len(l) - (i + 2)]
    line2 = l[i]
    for j in range(9):
        #the index to add to the stack
        ind = (4 * j) + 1
        #appends the alphabet to the stack
        if(line[ind] != " "):
            stacks[j].append(line[ind])
        if(line2[ind] != " "):
            queues[j].append(line2[ind])
    


for i in l2:
    instruction = i.split(" ")
    fromStack = int(instruction[3]) - 1
    toStack = int(instruction[5].removesuffix("\n")) - 1
    for j in range(int(instruction[1])):
        stacks[toStack].append(stacks[fromStack].pop())
        queues[toStack].insert(0, queues[fromStack].pop(int(instruction[1]) - (j + 1)))

str = ""
for i in range(9):
    #print(stacks[i].pop())
    str += queues[i].pop(0)
print(str)
