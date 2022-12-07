
if __name__ == "__main__":
    with open("Input.txt") as f:
        for line in f:
            line = line.replace("\n", "")
            range1, range2 = line.split(",")