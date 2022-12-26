if __name__ == "__main__":
    maze = []
    north_blizzards = []
    east_blizzards = []
    south_blizzards = []
    west_blizzards = []
    visitable_locations = []
    with open("Input.txt") as f:
        for y, line in enumerate(f):
            line = line.strip()
            maze.append([])
            for x, char in enumerate(line):
                if char == "^":
                    maze[-1].append(".")
                    north_blizzards.append((x, y))
                    visitable_locations.append((x, y))
                elif char == ">":
                    maze[-1].append(".")
                    east_blizzards.append((x, y))
                    visitable_locations.append((x, y))
                elif char == "v":
                    maze[-1].append(".")
                    south_blizzards.append((x, y))
                    visitable_locations.append((x, y))
                elif char == "<":
                    maze[-1].append(".")
                    west_blizzards.append((x, y))
                    visitable_locations.append((x, y))
                elif char == ".":
                    maze[-1].append(".")
                    visitable_locations.append((x, y))
                else:
                    maze[-1].append(char)

    start_location = (1, 0)
    end_location = (len(maze[0]) - 2, len(maze) - 1)
    target_location = end_location

    max_x = len(maze[0]) - 2
    max_y = len(maze) - 2
    
    end_reached = False
    locations_to_check = [start_location]
    seen_states = set()
    minutes_needed = 0

    seen_states.add((start_location, frozenset(north_blizzards), frozenset(south_blizzards), frozenset(east_blizzards), frozenset(west_blizzards)))

    trip_counter = 1

    while not end_reached:
        minutes_needed += 1

        # Move all the blizzards around
        for i, blizzard in enumerate(north_blizzards):
           if blizzard[1] == 1: new_y = max_y
           else: new_y = blizzard[1] - 1
           north_blizzards[i] = (blizzard[0], new_y)

        for i, blizzard in enumerate(south_blizzards):
           if blizzard[1] == max_y: new_y = 1
           else: new_y = blizzard[1] + 1
           south_blizzards[i] = (blizzard[0], new_y)

        for i, blizzard in enumerate(east_blizzards):
           if blizzard[0] == max_x: new_x = 1
           else: new_x = blizzard[0] + 1
           east_blizzards[i] = (new_x, blizzard[1])

        for i, blizzard in enumerate(west_blizzards):
           if blizzard[0] == 1: new_x = max_x
           else: new_x = blizzard[0] - 1
           west_blizzards[i] = (new_x, blizzard[1])

        NF = frozenset(north_blizzards)
        SF = frozenset(south_blizzards)
        EF = frozenset(east_blizzards)
        WF = frozenset(west_blizzards)
            
        # Check each possible direction move, or wait
        current_locations = locations_to_check
        locations_to_check = set()
        for location in current_locations:
            N = (location[0], location[1] - 1)
            S = (location[0], location[1] + 1)
            E = (location[0] + 1, location[1])
            W = (location[0] - 1, location[1])

            # We can only move south or north into the finish
            if S == target_location or N == target_location:
                if trip_counter == 3:
                    end_reached = True
                    break
                else:
                    trip_counter += 1
                    seen_states = set()
                    seen_states.add((target_location, NF, SF, EF, WF))
                    locations_to_check = [target_location]
                    if target_location == end_location: target_location = start_location
                    else: target_location = end_location
                    break

            # Check which of the locations we could move to (including if we can stay still!)
            move_north = not N in NF and not N in SF and not N in EF and not N in WF and N in visitable_locations
            move_south = not S in NF and not S in SF and not S in EF and not S in WF and S in visitable_locations
            move_east = not E in NF and not E in SF and not E in EF and not E in WF and E in visitable_locations
            move_west = not W in NF and not W in SF and not W in EF and not W in WF and W in visitable_locations
            stay_still = not location in NF and not location in SF and not location in EF and not location in WF and location in visitable_locations
          
            # Check if we've seen the state we'll end up in if we take the move
            if move_north and not (move_north, NF, SF, EF, WF) in seen_states:
                locations_to_check.add(N)
                seen_states.add((N, NF, SF, EF, WF))

            if move_south and not (move_south, NF, SF, EF, WF) in seen_states:
                locations_to_check.add(S)
                seen_states.add((S, NF, SF, EF, WF))

            if move_east and not (move_east, NF, SF, EF, WF) in seen_states:
                locations_to_check.add(E)
                seen_states.add((E, NF, SF, EF, WF))

            if move_west and not (move_west, NF, SF, EF, WF) in seen_states:
                locations_to_check.add(W)
                seen_states.add((W, NF, SF, EF, WF))

            if stay_still and not (stay_still, NF, SF, EF, WF) in seen_states:
                locations_to_check.add(location)
                seen_states.add((location, NF, SF, EF, WF))            

    print(minutes_needed)
