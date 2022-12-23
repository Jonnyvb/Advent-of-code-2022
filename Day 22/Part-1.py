if __name__ == "__main__":
    maze = []
    start_found = False
    current_location = (0, 0)
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

                maze.append([])
                for j, char in enumerate(line):
                    if not start_found and char == ".":
                        current_location = (j, i)
                        start_found = True

                    if char == " ":
                        maze[i].append("@")
                    else:
                        maze[i].append(char)
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


    max_col = max(len(row) for row in maze)
    max_row = len(maze)

    # Pad all our rows to be the same length
    for row in maze:
        row_len = len(row)
        for _ in range(max_col - row_len):
            row.append("@")

    for direction in directions:
        if direction == "L":
            current_direction = (current_direction - 1) % 4
        elif direction == "R":
            current_direction = (current_direction + 1) % 4
        else:
            for _ in range(direction):
                next_location_found = False
                test_location = current_location
                while not next_location_found:
                    if current_direction == 0:
                        next_location = (test_location[0] + 1, test_location[1])
                    elif current_direction == 1:
                        next_location = (test_location[0], test_location[1] + 1)
                    elif current_direction == 2:
                        next_location = (test_location[0] - 1, test_location[1])
                    elif current_direction == 3:
                        next_location = (test_location[0], test_location[1] - 1)
                    
                    # Wrap coordinates to be within the maze
                    next_location = (next_location[0] % max_col, next_location[1] % max_row)

                    if maze[next_location[1]][next_location[0]] == ".":
                        # If the square is empty, we can move to it and we're done
                        current_location = next_location
                        next_location_found = True
                    elif maze[next_location[1]][next_location[0]] == "#":
                        # If we're blocked by a wall, we're as far as we can go
                        next_location_found = True
                    else:
                        # We've hit a wrapping "@", we need to keep going until we find someting else
                        test_location = next_location
                        pass

    final_password = (1000 * (current_location[1] + 1)) + (4 * (current_location[0] + 1)) + current_direction
    print(final_password)