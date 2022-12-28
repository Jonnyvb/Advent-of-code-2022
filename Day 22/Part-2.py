if __name__ == "__main__":
    maze_faces = {}
    current_face = 0
    start_found = False
    current_location = (0, 0, 0)
    current_direction = 0 # 0: Right, 1: Down, 2: Left. 3: Up
    maze_finished = False
    directions = []
    with open("Input.txt") as f:
        for i, line in enumerate(f):
            line = line.replace("\n", "")
            if not maze_finished:
                if line == "":
                    maze_finished = True
                    continue

                for j, char in enumerate(line):
                    current_face = ((i // 50) * 3) + (j // 50)

                    if not start_found and char == ".":
                        current_location = (current_face, j % 50, i % 50)
                        start_found = True

                    if char != " ":

                        if current_face not in maze_faces:
                            maze_faces[current_face] = [[]]
                            maze_faces[current_face][-1].append(char)
                        else:
                            if len(maze_faces[current_face][-1]) % 50 == 0:
                                maze_faces[current_face].append([])

                            maze_faces[current_face][-1].append(char)
            else:
                char_str = ""
                for char in line:
                    if char.isdigit():
                        char_str += char
                    else:
                        directions.append(int(char_str))
                        directions.append(char)
                        char_str = ""
                
                if char_str != "":
                    directions.append(int(char_str))

    # Define the transitions ((face, edge), (face, edge))
    transitions = [
        ((1, 0), (9, 3), False),
        ((1, 1), (2, 3), False),
        ((1, 2), (4, 0), False),
        ((1, 3), (6, 3), True),
        ((2, 0), (9, 2), False),
        ((2, 1), (7, 1), True),
        ((2, 2), (4, 1), False),
        ((2, 3), (1, 1), False),
        ((4, 0), (1, 2), False),
        ((4, 1), (2, 2), False),
        ((4, 2), (7, 0), False),
        ((4, 3), (6, 0), False),
        ((6, 0), (4, 3), False),
        ((6, 1), (7, 3), False),
        ((6, 2), (9, 0), False),
        ((6, 3), (1, 3), True),
        ((7, 0), (4, 2), False),  
        ((7, 1), (2, 1), True),
        ((7, 2), (9, 1), False),
        ((7, 3), (6, 1), False),
        ((9, 0), (6, 2), False),
        ((9, 1), (7, 2), False),
        ((9, 2), (2, 0), False),
        ((9, 3), (1, 0), False),
    ]

    for direction in directions:
        if direction == "L":
            current_direction = (current_direction - 1) % 4
        elif direction == "R":
            current_direction = (current_direction + 1) % 4
        else:
            for _ in range(direction):
                current_face = current_location[0]
                x = current_location[1]
                y = current_location[2]
                if current_direction == 3 and y == 0:
                    transition = next(t for t in transitions if t[0][0] == current_face and t[0][1] == 0)
                elif current_direction == 0 and x == 49:
                    transition = next(t for t in transitions if t[0][0] == current_face and t[0][1] == 1)
                elif current_direction == 1 and y == 49:
                    transition = next(t for t in transitions if t[0][0] == current_face and t[0][1] == 2)
                elif current_direction == 2 and x == 0:
                    transition = next(t for t in transitions if t[0][0] == current_face and t[0][1] == 3)
                else:
                    # We're staying on the same face, lets handle this separately 
                    if current_direction == 0:
                        x += 1
                    elif current_direction == 1:
                        y += 1
                    elif current_direction == 2:
                        x -= 1
                    elif current_direction == 3:
                        y -= 1

                    if maze_faces[current_face][y][x] != "#":
                        current_location = (current_face, x, y)
                        continue
                    else:
                        break

                potential_face = transition[1][0]
                current_edge = transition[0][1]
                new_edge = transition[1][1]
                invert = transition[2]
                if (current_edge, new_edge) == (0, 0):
                    if invert:
                        x = 49 - x
                    potential_direction = 1
                elif (current_edge, new_edge) == (0, 1):
                    potential_direction = 2
                    if invert:
                        y = 49 - x
                    else:
                        y = x
                    x = 49
                elif (current_edge, new_edge) == (0, 2):
                    potential_direction = 3
                    if invert:
                        x = 49 - x
                    y = 49
                elif (current_edge, new_edge) == (0, 3):
                    potential_direction = 0
                    if invert:
                        y = 49 - x
                    else:
                        y = x
                    x = 0
                elif (current_edge, new_edge) == (1, 0):
                    potential_direction = 1
                    if invert:
                        x = 49 - y
                    else:
                        x = y
                    y = 0
                elif (current_edge, new_edge) == (1, 1):
                    potential_direction = 2
                    if invert:
                        y = 49 - y
                elif (current_edge, new_edge) == (1, 2):
                    potential_direction = 3
                    if invert:
                        x = 49 - y
                    else:
                        x = y
                    y = 49
                elif (current_edge, new_edge) == (1, 3):
                    potential_direction = 0
                    if invert:
                        y = 49 - y
                    x = 0
                elif (current_edge, new_edge) == (2, 0):
                    potential_direction = 1
                    if invert:
                        x = 49 - x
                    y = 0
                elif (current_edge, new_edge) == (2, 1):
                    potential_direction = 2
                    if invert:
                        y = 49 - y
                    else:
                        y = x
                    x = 49
                elif (current_edge, new_edge) == (2, 2):
                    if invert:
                        y = 49 - y
                    potential_direction = 3
                elif (current_edge, new_edge) == (2, 3):
                    potential_direction = 0
                    if invert:
                        y = 49 - x
                    else:
                        y = x
                    x = 0
                elif (current_edge, new_edge) == (3, 0):
                    potential_direction = 1
                    if invert:
                        x = 49 - y
                    else:
                        x = y
                    y = 0
                elif (current_edge, new_edge) == (3, 1):
                    potential_direction = 2
                    if invert:
                        y = 49 - y
                    x = 49
                elif (current_edge, new_edge) == (3, 2):
                    potential_direction = 3
                    if invert:
                        x = 49 - y
                    else:
                        x = y
                    y = 49
                elif (current_edge, new_edge) == (3, 3):
                    potential_direction = 0
                    if invert:
                        y = 49 - y

                if maze_faces[potential_face][y][x] != "#":
                    current_location = (potential_face, x, y)
                    current_direction = potential_direction
                else:
                    break

    current_row = ((current_location[0] // 3) * 50) + current_location[2]
    current_col = ((current_location[0] % 3) * 50) + current_location[1]

    final_password = (1000 * (current_row + 1)) + (4 * (current_col + 1)) + current_direction
    print(final_password)