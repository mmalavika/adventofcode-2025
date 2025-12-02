def partOne(inp):
    dial = 50
    zeroCount = 0
    for x in inp:
        dir = x[0]
        ticks = int(x[1:])
        if(dir == 'R'):
            dial += ticks
        else:
            dial -= ticks
        if(dial % 100 == 0): 
            zeroCount += 1
    return zeroCount

def partTwo(inp):
    dial = 50
    zeroCount = 0
    for x in inp:
        dir = x[0]
        ticks = int(x[1:])
        for i in range(0, ticks):
            if(dir == 'R'):
                dial += 1
            else: 
                dial -= 1
            if(dial % 100 == 0):
                zeroCount += 1
    return zeroCount

with open('day01/input.txt') as f:
    file_input = f.readlines()

print("Part One:", partOne(file_input))
print("Part Two:", partTwo(file_input))