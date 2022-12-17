if __name__ == "__main__":

    # Y index is reversed (we fall up), so rocks look upsidedown
    rocks = [
        [["#", "#", "#", "#"]],

        [[".", "#", "."],
         ["#", "#", "#"],
         [".", "#", "."]],

        [["#", "#", "#"],
         [".", ".", "#"],
         [".", ".", "#"]],

        [["#"],
         ["#"],
         ["#"],
         ["#"]],

        [["#", "#"],
         ["#", "#"]]
    ]

    chamber = [["#" for _ in range(7)] for _ in range(1)]
    highest_rock_level = 0

    with open("Input.txt") as f:
        jet_pattern = []
        for line in f: 
            line = line.strip()
            for char in line:
                jet_pattern.append(char)
    
    fallen_rocks = 0
    movements_made = 0
    while fallen_rocks < 2022:
        # Calculate indices to use for everything
        rock_type = fallen_rocks % len(rocks)
        fallen_rocks += 1
        
        # Look at our rock and expand our chamber as needed
        rock = rocks[rock_type]
        rock_height = len(rock)
        chamber_height_required = highest_rock_level + rock_height + 4
        if len(chamber) < chamber_height_required:
            chamber.extend([["." for _ in range(7)] for _ in range(chamber_height_required - len(chamber))])

        # Keep track of the rocks top left position (y, x)
        # Always spawns in 3 above the highest rock level and 2 in from left
        rock_position = (highest_rock_level + 5, 2)
        rock_settled = False
        while not rock_settled:
            # First the rock falls
            move_good = True
            for x in range(len(rock[0])):
                for y in range(len(rock)):
                    char = rock[y][x]
                    if char == "#":
                        if chamber[rock_position[0] + y - 1][rock_position[1] + x] == "#":
                            move_good = False
                        break
                if not move_good:
                    break
            
            if move_good:
                rock_position = (rock_position[0] - 1, rock_position[1])
            else:
                rock_settled = True
                # Add rock to chamber
                highest_rock_level = max(highest_rock_level, rock_position[0] + len(rock) - 1)
                for y in range(len(rock)):
                    for x in range(len(rock[0])):
                        if rock[y][x] == "#":
                            chamber_y = rock_position[0] + y
                            chamber_x = rock_position[1] + x
                            chamber[chamber_y][chamber_x] = "#"

            if rock_settled:
                break

            # Now we apply the jet stream
            jet_direction = jet_pattern[movements_made % len(jet_pattern)]
            move_good = True
            if jet_direction == "<":
                # Check if we're not at the left edge of the chamber
                if rock_position[1] != 0:
                    # Now we have to check to the left of each rock segment
                    for y, line in enumerate(rock):
                        for x, char in enumerate(line):
                            if char == "#":
                                if chamber[rock_position[0] + y][rock_position[1] + x - 1] == "#":
                                    move_good = False
                                break
                        if not move_good:
                            break
                else:
                    move_good = False

                if move_good:
                    rock_position = (rock_position[0], rock_position[1] - 1)
            else:
                # Check if we're not at the right edge of the chamber
                if rock_position[1] + len(rock[0]) != len(chamber[0]):
                    # Now we have to check to the left of each rock segment
                    for y, line in enumerate(rock):
                        for x, char in enumerate(reversed(line)):
                            if char == "#":
                                if chamber[rock_position[0] + y][rock_position[1] + (len(line) - x)] == "#":
                                    move_good = False
                                break
                        if not move_good:
                            break
                else:
                    move_good = False

                if move_good:
                    rock_position = (rock_position[0], rock_position[1] + 1)
            
            movements_made += 1

    print(highest_rock_level)