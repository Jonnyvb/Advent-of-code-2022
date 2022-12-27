if __name__ == "__main__":
    north_blizzards = []
    east_blizzards = []
    south_blizzards = []
    west_blizzards = []
    visitable_locations = set()
    with open("Input.txt") as f:
        for y, line in enumerate(f):
            line = line.strip()
            for x, char in enumerate(line):
                if char == "^":
                    north_blizzards.append((x, y))
                    visitable_locations.add((x, y))
                elif char == ">":
                    east_blizzards.append((x, y))
                    visitable_locations.add((x, y))
                elif char == "v":
                    south_blizzards.append((x, y))
                    visitable_locations.add((x, y))
                elif char == "<":
                    west_blizzards.append((x, y))
                    visitable_locations.add((x, y))
                elif char == ".":
                    visitable_locations.add((x, y))

    maze_width = max([location[0] for location in visitable_locations])
    maze_height = max([location[1] for location in visitable_locations])

    start_location = (1, 0)
    end_location = (maze_width, maze_height)
    
    end_reached = False
    locations_to_check = [start_location]
    seen_states = set()
    minutes_needed = 0

    blizzard_period = (maze_height - 1) * (maze_width - 1)

    seen_states.add((start_location, minutes_needed % blizzard_period))

    while not end_reached:
        minutes_needed += 1

        # Move all the blizzards around
        for i, blizzard in enumerate(north_blizzards):
           if blizzard[1] == 1: new_y = maze_height - 1
           else: new_y = blizzard[1] - 1
           north_blizzards[i] = (blizzard[0], new_y)

        for i, blizzard in enumerate(south_blizzards):
           if blizzard[1] == maze_height - 1: new_y = 1
           else: new_y = blizzard[1] + 1
           south_blizzards[i] = (blizzard[0], new_y)

        for i, blizzard in enumerate(east_blizzards):
           if blizzard[0] == maze_width: new_x = 1
           else: new_x = blizzard[0] + 1
           east_blizzards[i] = (new_x, blizzard[1])

        for i, blizzard in enumerate(west_blizzards):
           if blizzard[0] == 1: new_x = maze_width
           else: new_x = blizzard[0] - 1
           west_blizzards[i] = (new_x, blizzard[1])

        NF = set(north_blizzards)
        SF = set(south_blizzards)
        EF = set(east_blizzards)
        WF = set(west_blizzards)
            
        # Check each possible direction move, or wait
        current_locations = locations_to_check
        locations_to_check = set()
        for location in current_locations:
            N = (location[0], location[1] - 1)
            S = (location[0], location[1] + 1)
            E = (location[0] + 1, location[1])
            W = (location[0] - 1, location[1])

            # We can only move south into the finish
            if S == end_location:
                end_reached = True
                break

            # Check which of the locations we could move to (including if we can stay still!)
            move_north = not N in NF and not N in SF and not N in EF and not N in WF and N in visitable_locations
            move_south = not S in NF and not S in SF and not S in EF and not S in WF and S in visitable_locations
            move_east = not E in NF and not E in SF and not E in EF and not E in WF and E in visitable_locations
            move_west = not W in NF and not W in SF and not W in EF and not W in WF and W in visitable_locations
            stay_still = not location in NF and not location in SF and not location in EF and not location in WF and location in visitable_locations
          
            # Check if we've seen the state we'll end up in if we take the move
            if move_north and not (move_north, minutes_needed % blizzard_period) in seen_states:
                locations_to_check.add(N)
                seen_states.add((N, minutes_needed % blizzard_period))

            if move_south and not (move_south, minutes_needed % blizzard_period) in seen_states:
                locations_to_check.add(S)
                seen_states.add((S, minutes_needed % blizzard_period))

            if move_east and not (move_east, minutes_needed % blizzard_period) in seen_states:
                locations_to_check.add(E)
                seen_states.add((E, minutes_needed % blizzard_period))

            if move_west and not (move_west, minutes_needed % blizzard_period) in seen_states:
                locations_to_check.add(W)
                seen_states.add((W, minutes_needed % blizzard_period))

            if stay_still and not (stay_still, minutes_needed % blizzard_period) in seen_states:
                locations_to_check.add(location)
                seen_states.add((location, minutes_needed % blizzard_period))            

    print(minutes_needed)
