f = open("06.txt", "r")
l = f.read()
counter = 0
chars = []
conflict = 0
length = 14
for i in l:
    if counter <= (length - 2):
        chars.append(i)
        counter += 1
    else:
        if(i not in chars):
            if(conflict <= 0):
                counter += 1
                break
            else:
                conflict -= 1
                chars.pop(0)
                chars.append(i)
                counter+=1
        else:
            temp = (length - 1) - chars[::-1].index(i)
            if(temp > conflict):
                conflict = temp
            counter += 1
            chars.pop(0)
            chars.append(i)
            conflict -= 1
print(counter)