if __name__ == "__main__":
    with open("Input.txt") as f:
        trees = []
        for line in f:
            line = line.replace("\n", "")
            treeRow = []
            for tree in line:
                treeRow.append(int(tree))

            trees.append(treeRow)

    visibleTreeCount = 0
    visibleTrees = []
    for rowIndex, row in enumerate(trees):
        for columnIndex, treeHeight in enumerate(row):
            # Iterate each tree, then approach from each direction to see
            # if it's visible
            # Edge trees are always visible
            if rowIndex == 0 or columnIndex == 0 or rowIndex == len(trees) - 1 or columnIndex == len(trees[0]) - 1:
                visibleTreeCount += 1
                visibleTrees.append([rowIndex, columnIndex])
                continue
            else:
                # First check to the left
                for compareTreeHeight in trees[rowIndex][:columnIndex]:
                    if compareTreeHeight >= treeHeight:
                        break
                else:
                    visibleTreeCount += 1
                    visibleTrees.append([rowIndex, columnIndex])
                    continue

                # then the right
                for compareTreeHeight in trees[rowIndex][columnIndex + 1:]:
                    if compareTreeHeight >= treeHeight:
                        break
                else:
                    visibleTreeCount += 1
                    visibleTrees.append([rowIndex, columnIndex])
                    continue

                # then from above
                for compareTreeHeight in trees[:rowIndex]:
                    if compareTreeHeight[columnIndex] >= treeHeight:
                        break
                else:
                    visibleTreeCount += 1
                    visibleTrees.append([rowIndex, columnIndex])
                    continue

                # and finally from below
                for compareTreeHeight in trees[rowIndex + 1:]:
                    if compareTreeHeight[columnIndex] >= treeHeight:
                        break
                else:
                    visibleTreeCount += 1
                    visibleTrees.append([rowIndex, columnIndex])
                    continue
    
    print(visibleTrees)
    print(visibleTreeCount)