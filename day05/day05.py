def partOne(ranges, ids):
    fresh = set()
    for x in ids:
        for rng in ranges:
            rngStart, rngStop = rng.split("-")
            if(int(x) in range(int(rngStart), int(rngStop))):
                fresh.add(int(x))
    return len(fresh)

def partTwo(inp):
    ranges = []
    for r in inp:
        ranges.append(tuple(map(int, r.split("-"))))
    ranges.sort()
    rStart, rStop = ranges[0]
    intervals = []
    for rn in ranges[1:]:
        nextStart = rn[0]
        nextStop = rn[1]
        if(rStart <= nextStart and nextStop <= rStop):
            continue
        if(nextStart <= rStop):
            rStop = max(nextStop, rStop)
        else:
            intervals.append((rStart, rStop))
            rStart = nextStart
            rStop = nextStop
    intervals.append((rStart, rStop))
    
    sum = 0
    for inv in intervals:
        sum += (inv[1]+1)-inv[0]
    return sum

with open('day05/input-range.txt') as f:
    input_ranges = f.readlines()

with open('day05/input-ids.txt') as f:
    input_ids = f.readlines()

print("Part One:", partOne(input_ranges, input_ids))
print("Part Two:", partTwo(input_ranges))