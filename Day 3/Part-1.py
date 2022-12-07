
if __name__ == "__main__":
    with open("./Day 3/Input.txt") as f:
        priority = 0
        for line in f:
            line = line.replace("\n", "")
            itemCount = len(line)
            compartment1 = line[:(itemCount//2)]
            compartment2 = line[(itemCount//2):]

            overlap = set(compartment1).intersection(compartment2)
            print(overlap)

            for item in overlap:
                val = ord(item)
                if val >= 97:
                    priority += val - 96
                else:
                    priority += val - 38

    print(priority)