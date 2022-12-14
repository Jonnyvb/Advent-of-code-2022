def print_cave(cave, min_x, max_x, max_y):
    for row in cave[:max_y + 1]:
            for col in row[min_x:max_x + 1]:
                print(col, end="")
            print()

if __name__ == "__main__":
    with open("Input.txt") as f:
        paths = []
        max_x_coord = 0
        min_x_coord = 100000
        max_y_coord = 0
        for line in f:
            line = line.strip()

            path_points = line.split(" -> ")

            # We need to iterate pairs of points to make lines, so stop one before the end
            for i in range(len(path_points) - 1):
                start_x, start_y = path_points[i].split(",")
                end_x, end_y = path_points[i + 1].split(",")

                start_x = int(start_x)
                start_y = int(start_y)
                end_x = int(end_x)
                end_y = int(end_y)

                paths.append([(start_x, start_y), (end_x, end_y)])

                min_x_coord = min(min_x_coord, start_x, end_x)
                max_x_coord = max(max_x_coord, start_x, end_x)
                max_y_coord = max(max_y_coord, start_y, end_y)

        # Create a grid to represent our cave
        cave = [["." for x in range(max_x_coord + 2)] for y in range(max_y_coord + 2)]

        for path in paths:
            start_x = min(path[0][0], path[1][0])
            start_y = min(path[0][1], path[1][1])
            end_x = max(path[0][0], path[1][0])
            end_y = max(path[0][1], path[1][1])

            print(f"Drawing from {start_x} to {end_x} and {start_y} to {end_y}")

            for x in range(start_x, end_x + 1):
                for y in range(start_y, end_y + 1):
                    cave[y][x] = "#"

        bottom_reached = False
        sand_added = 0
        sand_start = (500, 0)
        while not bottom_reached:
            # Add a new sand particle and follow it down!
            sand_settled = False
            sand_location = sand_start
            print(f"Added sand {sand_added}")
            while not sand_settled:
                # Check if we can move directly down
                # if not, try down left diagonal, then down right
                sand_x = sand_location[0]
                sand_y = sand_location[1]
                if sand_y >= max_y_coord:
                    # Check if we're falling off the bottom
                    bottom_reached = True
                    break
                elif cave[sand_y + 1][sand_x] == ".":
                    sand_location = (sand_x, sand_y + 1)
                elif cave[sand_y + 1][sand_x - 1] == ".":
                    sand_location = (sand_x - 1, sand_y + 1)
                elif cave[sand_y + 1][sand_x + 1] == ".":
                    sand_location = (sand_x + 1, sand_y + 1)
                else:
                    # Indicate we've settled and update the cave to show this
                    cave[sand_y][sand_x] = "O"
                    sand_settled = True
                    sand_added += 1

        print_cave(cave, min_x_coord, max_x_coord, max_y_coord)
        print(sand_added)
