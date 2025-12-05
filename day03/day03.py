def partOne(inp):
    sum = 0
    for ln in inp:
        nums = list(ln.strip())
        first = max(nums)
        firstIdx = nums.index(first)
        if(firstIdx+1 == len(nums)):
            second = first
            first = max(nums[:firstIdx])
        else:
            second = max(nums[firstIdx+1:])
        m = first + second
        sum += int(m)
    return sum

def partTwo(inp):
    sum = 0
    twelves = []
    for ln in inp:
        twelve = ''
        nums = ln.strip()
        start = 0
        for i in range(1, 13):
            stop = len(nums)-(12-i)
            highest = max(nums[start:stop])
            twelve += highest
            start += nums[start:].index(highest)+1
        sum += int(twelve)
        twelves.append(twelve)
    return sum

with open('day03/input.txt') as f:
    file_input = f.readlines()

print("Part One:", partOne(file_input))
print("Part Two:", partTwo(file_input))