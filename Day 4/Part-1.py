
if __name__ == "__main__":
    with open("Input.txt") as f:
        overlapCount = 0
        for line in f:
            line = line.replace("\n", "")
            range1, range2 = line.split(",")
            range1Lower, range1Upper = range1.split("-")
            range2Lower, range2Upper = range2.split("-")
            range1Lower = int(range1Lower)
            range1Upper = int(range1Upper)
            range2Lower = int(range2Lower)
            range2Upper = int(range2Upper)

            if ((range1Lower <= range2Lower and range1Upper >= range2Upper)
                or (range2Lower <= range1Lower and range2Upper >= range1Upper)):
                overlapCount += 1

    print(overlapCount)