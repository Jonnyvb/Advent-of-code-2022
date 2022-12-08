if __name__ == "__main__":
    with open("Input.txt") as f:
        trees = []
        for line in f:
            line = line.replace("\n", "")
            treeRow = []
            for tree in line:
                treeRow.append(int(tree))

            trees.append(treeRow)

    highestScenicScore = 0
    for rowIndex, row in enumerate(trees):
        for columnIndex, treeHeight in enumerate(row):
            # Iterate each tree, then approach from each direction to see
            # its visibility score
            
            leftVisibility = 0
            rightVisibility = 0
            topVisibility = 0
            bottomVisibility = 0

            # First check to the left, moving away from our tree
            for compareTreeHeight in reversed(trees[rowIndex][:columnIndex]):
                leftVisibility += 1
                if compareTreeHeight >= treeHeight:
                    break

            # then the right
            for compareTreeHeight in trees[rowIndex][columnIndex + 1:]:
                rightVisibility += 1
                if compareTreeHeight >= treeHeight:
                    break

            # then from above, moving away from our tree
            for compareTreeHeight in reversed(trees[:rowIndex]):
                topVisibility += 1
                if compareTreeHeight[columnIndex] >= treeHeight:
                    break

            # and finally from below
            for compareTreeHeight in trees[rowIndex + 1:]:
                bottomVisibility += 1
                if compareTreeHeight[columnIndex] >= treeHeight:
                    break

            scenicScore = leftVisibility * rightVisibility * topVisibility * bottomVisibility
            if scenicScore > highestScenicScore:
                highestScenicScore = scenicScore
    
    print(highestScenicScore)