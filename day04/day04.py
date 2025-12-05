def partOne(inp):
    count = 0
    for row, ln in enumerate(inp):
        l = list(ln.strip())
        for col, ch in enumerate(l):
            if(ch == '@'):
                adjacent = []
                if(row-1 >= 0):
                    adjacent.append(inp[row-1][col])
                if(row+1 < len(inp)):
                    adjacent.append(inp[row+1][col])
                if(col-1 >= 0):
                    adjacent.append(l[col-1])
                if(col+1 < len(l)):
                    adjacent.append(l[col+1])
                if(row-1 >= 0 and col-1 >= 0):
                    adjacent.append(inp[row-1][col-1])
                if(row-1 >= 0 and col+1 < len(l)):
                    adjacent.append(inp[row-1][col+1])
                if(row+1 < len(inp) and col-1 >= 0):
                    adjacent.append(inp[row+1][col-1])
                if(row+1 < len(inp) and col+1 < len(l)):
                    adjacent.append(inp[row+1][col+1])
                if(adjacent.count('@') < 4):
                    count += 1
    return count

def partTwo(inp):
    ct, clean = cleanup(inp)
    while ct != 0:
        ct, clean = cleanup(clean)
    count = 0
    for ln in clean:
        count += ln.count('x')
    return count

def cleanup(inp):
    inpCpy = inp.copy()
    count = 0
    for row, ln in enumerate(inp):
        l = list(ln.strip())
        for col, ch in enumerate(l):
            if(ch == '@'):
                adjacent = []
                if(row-1 >= 0):
                    adjacent.append(inp[row-1][col])
                if(row+1 < len(inp)):
                    adjacent.append(inp[row+1][col])
                if(col-1 >= 0):
                    adjacent.append(l[col-1])
                if(col+1 < len(l)):
                    adjacent.append(l[col+1])
                if(row-1 >= 0 and col-1 >= 0):
                    adjacent.append(inp[row-1][col-1])
                if(row-1 >= 0 and col+1 < len(l)):
                    adjacent.append(inp[row-1][col+1])
                if(row+1 < len(inp) and col-1 >= 0):
                    adjacent.append(inp[row+1][col-1])
                if(row+1 < len(inp) and col+1 < len(l)):
                    adjacent.append(inp[row+1][col+1])
                if(adjacent.count('@') < 4):
                    count += 1
                    lCpy = l.copy()
                    lCpy[col] = 'x'
                    inpCpy[row] = ''.join(lCpy)
    return [count, inpCpy]

with open('day04/input.txt') as f:
    file_input = f.readlines()

print("Part One:", partOne(file_input))
print("Part Two:", partTwo(file_input))