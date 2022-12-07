
def OrderdedInsert(insertList, value):
    # Find the palce to insert
    for i, arrayVal in enumerate(insertList):
        if value > arrayVal:
            insertList.insert(i, value)
            insertList.pop(len(insertList) - 1)
            break
        
if __name__ == "__main__":
    with open(r"./Day 1/Day-1-Input.txt") as f:
        maxCalories = [0, 0, 0]
        thisElfCalories = 0
        for line in f:
            line = line.replace("\n", "")
            if not line:
                OrderdedInsert(maxCalories, thisElfCalories)
                thisElfCalories = 0
            else:
                thisElfCalories += int(line)

        print(maxCalories)
        print(sum(maxCalories))