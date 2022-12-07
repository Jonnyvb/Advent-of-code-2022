if __name__ == "__main__":
    with open("Input.txt") as f:
        crateStack = []
        for line in f:
            line = line.replace("\n", " ")

            if line.strip().startswith("["):
                n = 4
                crates = [line[i:i+n] for i in range(0, len(line), n)]
                
                while len(crateStack) < len(crates):
                    crateStack.append([])

                for i, crate in enumerate(crates):
                    if "[" in crate:
                        crateStack[i].insert(0, crate)
            elif line.startswith("move"):
                count, fromStack, toStack = [int(s) for s in line.split() if s.isdigit()]
                # Account for 0-based index
                fromStack -= 1
                toStack -= 1
                movingCrateStack = []
                while count != 0:
                    movingCrateStack.append(crateStack[fromStack].pop())
                    count -= 1
                
                while len(movingCrateStack) > 0:
                    crateStack[toStack].append(movingCrateStack.pop())

        print(crateStack)

        output = ""
        for stack in crateStack:
            output += stack[len(stack) - 1]

        output = output.replace("[", "").replace("]", "").replace(" ", "")
        print(output)