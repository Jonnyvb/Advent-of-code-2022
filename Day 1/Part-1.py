
if __name__ == "__main__":
    with open("Input.txt") as f:
        maxCalories = 0
        thisElfCalories = 0
        for line in f:
            line = line.replace("\n", "")
            if not line:
                if thisElfCalories > maxCalories:
                    maxCalories = thisElfCalories

                thisElfCalories = 0
            else:
                thisElfCalories += int(line)

        print(maxCalories)