def partOne(inp):
    sum = 0
    for rng in inp:
        x,y = rng.split("-")
        for i in range(int(x), int(y)+1):
            if(isValidId1(str(i)) == False):
                sum += i
    return sum

def partTwo(inp):
    sum = 0
    for rng in inp:
        x,y = rng.split("-")
        for i in range(int(x), int(y)+1):
            if(isValidId2(str(i)) == False):
                sum += i
    return sum

def isValidId1(id):
    if(len(id) % 2 == 0):
        halfIdx = len(id) // 2
        first = id[:halfIdx]
        last = id[halfIdx:]
        if(first == last):
            return False
        else:
            return True
    return True

def isValidId2(id):
    halfIdx = len(id) // 2
    for i in range(1, halfIdx+1):
        subStr = id[:i]
        oc = id.count(subStr)
        if(oc * i == len(id)):
            return False
    return True

with open('day02/input.txt') as f:
    file_input = f.readlines()
    inpList = file_input[0].split(",")

print("Part One:", partOne(inpList))
print("Part Two:", partTwo(inpList))