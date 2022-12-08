f = open("07.txt", "r").read().split("$ cd")
currentDir = ""
map = {}
f.pop(0)
for i in f:
    i = i.split("\n")
    #if we're going up a directory
    if(i[0] == " .."):
        currentDir = currentDir[:currentDir.rfind("/")]
        if(currentDir == ""):
            currentDir = "/"
    else:
        #set the current directory
        if(currentDir == "/" or currentDir == ""):
            currentDir = currentDir + i[0].strip()
        else:
            currentDir = currentDir + "/" + i[0].strip()
    #removes the first element since we're done with it
    i.pop(0)
    #removed the last element since it's empty
    i.pop()
    #create a new entry in the map for the current directory
    if(currentDir not in map):
        size = 0
        children = []
        for j in i:
            if(j.startswith("dir")):
                children.append(j.split(" ")[1])
            elif(j.startswith("$ ls")):
                pass
            else: size += int(j.split(" ")[0])
        map[currentDir] = [size, children]

#find size of all children
def getChildrenSize(dir):
    size = map[dir][0]
    for i in map[dir][1]:
        if(dir == "/"):
            dir = ""
        size += getChildrenSize(dir + "/" + i)
    return size

#part 1
total = 0
for i in map.keys():
    size = getChildrenSize(i)
    if(size < 100000):
        total += size

print(total)

#part 2
min = 111111111111111111111111111
spaceneeded = 30000000 - (70000000 - getChildrenSize("/"))
for i in map.keys():
    size = getChildrenSize(i)
    if(size > spaceneeded):
        if(size < min):
            min = size
print(min)