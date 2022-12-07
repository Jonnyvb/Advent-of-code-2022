
if __name__ == "__main__":
    with open("Input.txt") as f:
        priority = 0
        elfGroup = 0
        elfBag = ["", "" , ""]
        for line in f:
            line = line.replace("\n", "")
            elfBag[elfGroup] = line

            elfGroup += 1
            if elfGroup == 3:
                elfGroup = 0
                overlap = set(elfBag[0]).intersection(elfBag[1]).intersection(elfBag[2])

                for item in overlap:
                    val = ord(item)
                    if val >= 97:
                        priority += val - 96
                    else:
                        priority += val - 38

    print(priority)