def Print_Board(knots):
    x_board = [x for x in range(-11, 15)]
    y_board = [y for y in range(-5, 16)]
    for y in reversed(y_board):
        for x in x_board:
            for i, knot in enumerate(knots):
                if knot == (x, y):
                    if i == 0:
                        print("H", end="")
                    else:
                        print(i, end="")
                    break
            else:
                if (x, y) == (0, 0):
                    print("S", end="")
                else:
                    print(".", end="")
        print()
    print()

def Print_Visited(visited):
    # Find max and min board coordinates
    x_min = min(visited, key = lambda tup: tup[0])[0]
    x_max = max(visited, key = lambda tup: tup[0])[0]
    y_min = min(visited, key = lambda tup: tup[1])[1]
    y_max = max(visited, key = lambda tup: tup[1])[1]

    x_board = [x for x in range(x_min, x_max)]
    y_board = [y for y in range(y_min, y_max)]
    for y in reversed(y_board):
        for x in x_board:
            if (x, y) == (0, 0):
                print("S", end="")
            else:
                for knot in visited:
                    if knot == (x, y):
                        print("#", end="")
                        break
                else:
                    print(".", end="")
        print()
    print()

if __name__ == "__main__":
    with open("Input.txt") as f:
        # Coordinates as (x, y)
        knots = [(0, 0) for i in range(10)]
        tail_visited_coords = set()
        tail_visited_coords.add(knots[9])
        for line in f:
            line = line.replace("\n", "")
            direction, count = line.split(" ")

            for _ in range(int(count)):
                # Move the fist knot based on input
                if direction == "U":
                    knots[0] = (knots[0][0], knots[0][1] + 1)
                elif direction == "D":
                    knots[0] = (knots[0][0], knots[0][1] - 1)
                elif direction == "R":
                    knots[0] = (knots[0][0] + 1, knots[0][1])
                elif direction == "L":
                    knots[0] = (knots[0][0] - 1, knots[0][1])

                # Loop through the rest of the knots and update based on the previous
                for i, knot in enumerate(knots):
                    if i == 0:
                        continue

                    x_diff = knots[i - 1][0] - knot[0]
                    y_diff = knots[i - 1][1] - knot[1]

                    # Default to not moving
                    x_new_coord = knot[0]
                    y_new_coord = knot[1]

                    # Check if other coord needs to move too
                    if abs(x_diff) > 1 and abs(y_diff) > 1:
                        if x_diff > 0:
                            x_new_coord += 1
                        else:
                            x_new_coord -= 1

                        if y_diff > 0:
                            y_new_coord += 1
                        else:
                            y_new_coord -= 1
                    elif abs(x_diff) > 1 :
                        y_new_coord = knots[i - 1][1]
                    elif abs(y_diff) > 1:
                        x_new_coord = knots[i - 1][0]

                    if x_diff > 1:
                        x_new_coord = knot[0] + (x_diff - 1)
                    elif x_diff < -1:
                        x_new_coord = knot[0] + (x_diff + 1)
                    elif y_diff > 1:
                        y_new_coord = knot[1] + (y_diff - 1)
                    elif y_diff < -1:
                        y_new_coord = knot[1] + (y_diff + 1)

                    knots[i] = (x_new_coord, y_new_coord)

                #Print_Board(knots)
                tail_visited_coords.add(knots[9])
        
        Print_Visited(tail_visited_coords)
        print(len(tail_visited_coords))