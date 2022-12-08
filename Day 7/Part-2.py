
def ExploreDir(dirs, k, dir):
    totalSize = 0
    for path, size in dir.items():
        if size == 0:
            totalSize += ExploreDir(dirs, k + "/" + path, dirs[k + "/" + path])
        else:
            totalSize += size

    return totalSize


if __name__ == "__main__":
    with open("Input.txt") as f:
        pathCrumbs = ["/"]
        dirs = {"/" : {}}
        for line in f:
            line = line.replace("\n", " ")

            if line.startswith("$"):
                # User input commands
                if "cd" in line:
                    dest = line.split(" ")[2]

                    if dest == "/":
                        pathCrumbs.clear()
                        pathCrumbs.append("/")
                    elif dest == "..":
                        pathCrumbs.pop()
                    else:
                        pathCrumbs.append(dest)
                        pathSlug = "/".join(pathCrumbs)
                        if not pathSlug in dirs.keys():
                            dirs[pathSlug] = {}
            else:
                # System responses
                pathSlug = "/".join(pathCrumbs)
                path = line.split(" ")[1]
                if line.startswith("dir"):
                    dirs[pathSlug][path] = 0
                else:
                    size = line.split(" ")[0]
                    dirs[pathSlug][path] = int(size)

    dirSizes = {}
    for k, dir in dirs.items():
        dirSize = ExploreDir(dirs, k, dir)
        dirSizes[k] = dirSize

    # Total free space
    freeSpace = 70000000 - dirSizes["/"]
    spaceNeeded = 30000000 - freeSpace

    currentDirToDelete = {"name": "", "size": 70000000}
    for dir, size in dirSizes.items():
        if size >= spaceNeeded and size < currentDirToDelete["size"]:
            currentDirToDelete["name"] = dir
            currentDirToDelete["size"] = size

    print(spaceNeeded)
    print(currentDirToDelete["size"])
