
# 4-6, 7-9
# 4-6, 5-9
# 4-6, 3-9
# 4-6, 3-5
# 3-5, 4-6

def CheckOverlap(inputLine):
    range1, range2 = inputLine.split(",")
    range1Lower, range1Upper = range1.split("-")
    range2Lower, range2Upper = range2.split("-")
    range1Lower = int(range1Lower)
    range1Upper = int(range1Upper)
    range2Lower = int(range2Lower)
    range2Upper = int(range2Upper)

    range1 = list(range(range1Lower, range1Upper + 1))
    range2 = list(range(range2Lower, range2Upper + 1))

    overlap = set(range1).intersection(range2)

    return len(overlap) > 0

if __name__ == "__main__":
    with open("Input.txt") as f:
        overlapCount = 0
        for line in f:
            line = line.replace("\n", "")
            if CheckOverlap(line):
                overlapCount += 1
    print(overlapCount)