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
    rock_level_in_stack = 0

    total_rocks_to_fall = 1_000_000_000_000
    with open("Input.txt") as f:
        jet_pattern = []
        for line in f: 
            line = line.strip()
            for char in line:
                jet_pattern.append(char)

    fallen_rocks = 0
    movements_made = 0
    seen_tops = {}
    while fallen_rocks < total_rocks_to_fall:
        # Calculate indices to use for everything
        rock_type = fallen_rocks % len(rocks)
        fallen_rocks += 1

        # Look at our rock and expand our chamber as needed
        rock = rocks[rock_type]
        rock_height = len(rock)
        chamber_height_required = rock_level_in_stack + rock_height + 4
        if len(chamber) < chamber_height_required:
            chamber.extend([["." for _ in range(7)] for _ in range(chamber_height_required - len(chamber))])

        # Keep track of the rocks top left position (y, x)
        # Always spawns in 3 above the highest rock level (+2 to account floor thickness and initial drop) and 2 in from left
        rock_position = (rock_level_in_stack + 5, 2)
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
                highest_rock_level += (max(rock_level_in_stack, rock_position[0] + len(rock) - 1) - rock_level_in_stack)
                rock_level_in_stack = max(rock_level_in_stack, rock_position[0] + len(rock) - 1)
                for y in range(len(rock)):
                    for x in range(len(rock[0])):
                        if rock[y][x] == "#":
                            chamber_y = rock_position[0] + y
                            chamber_x = rock_position[1] + x
                            chamber[chamber_y][chamber_x] = "#"

            if rock_settled:
                break

            # Now we apply the jet stream
            jet_index = movements_made % len(jet_pattern)
            jet_direction = jet_pattern[jet_index]
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
            movements_made = movements_made % len(jet_pattern)

        # Record all tops we've seen and where we were in the rock/jet cycle to find a point where we repeat
        max_depth_found = False
        current_row = chamber[rock_level_in_stack]
        y_delta = 0
        accessible_x = [x for x, char in enumerate(current_row) if char == "."]
        while not max_depth_found:
            y_delta += 1
            current_row = chamber[rock_level_in_stack - y_delta]
            accessible_x = [x for x in accessible_x if current_row[x] == "." or (x > 0 and current_row[x - 1]) == "." or (x < 6 and current_row[x + 1] == ".")]
            if len(accessible_x) == 0:
                max_depth_found = True
        
        max_fall_depth = rock_level_in_stack - y_delta
        
        top_section = chamber[max_fall_depth:rock_level_in_stack + 1]
        hashable_top = str(top_section)
        if not (rock_type, jet_index, y_delta) in seen_tops:
            seen_tops[(rock_type, jet_index, y_delta)] = {}

        if hashable_top in seen_tops[(rock_type, jet_index, y_delta)]:
            # How many rocks have fallen since we last saw this?
            rocks_in_cycle = fallen_rocks - seen_tops[(rock_type, jet_index, y_delta)][hashable_top][0]
            height_gained = rock_level_in_stack - seen_tops[(rock_type, jet_index, y_delta)][hashable_top][1]
            rocks_left = total_rocks_to_fall - fallen_rocks
            full_cycles_left = rocks_left // rocks_in_cycle
            fallen_rocks += (full_cycles_left * rocks_in_cycle)
            highest_rock_level += (full_cycles_left * height_gained)

        else:
            seen_tops[(rock_type, jet_index, y_delta)][hashable_top] = (fallen_rocks, rock_level_in_stack)

    print(highest_rock_level)