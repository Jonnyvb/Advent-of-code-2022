def Print_Elf_Locations(elves):
    current_elf_locations = [elf["current_location"] for elf in elves]
    min_x = min([elf["current_location"][0] for elf in elves])
    max_x = max([elf["current_location"][0] for elf in elves])
    min_y = min([elf["current_location"][1] for elf in elves])
    max_y = max([elf["current_location"][1] for elf in elves])

    print("    ", end="")
    for x in range(min_x, max_x + 1):
        print(str(x).rjust(3, " ")[0], end="")
    print()
    print("    ", end="")
    for x in range(min_x, max_x + 1):
        print(str(x).rjust(3, " ")[1], end="")
    print()
    print("    ", end="")
    for x in range(min_x, max_x + 1):
        print(str(x).rjust(3, " ")[2], end="")
    print()

    for y in range(min_y, max_y + 1):
        print(f"{y:02d}: ", end="")
        for x in range(min_x, max_x + 1):
            if (x, y) in current_elf_locations:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()

from collections import Counter

if __name__ == "__main__":
    elves = []
    with open("Input.txt") as f:
        for i, line in enumerate(f):
            for j, char in enumerate(line):
                if char == "#":
                    # Store the elf's current location and its intended next one
                    elves.append({"current_location": (j, i), "proposed_location": (j, i)})
    
    # Store next direction, 0 for N, 1 for S, 2 for W, 3 for E
    elf_direction = 0

    # Keep going until we're done!
    round_count = 0
    current_elf_locations = set([elf["current_location"] for elf in elves])
    while True:
        # Find all the proposed elf moves
        proposed_moves_counter = Counter()
        for elf in elves:
            elf_location = elf["current_location"]

            # Find all the coordinates around this elf
            N = (elf_location[0], elf_location[1] - 1)
            NE = (elf_location[0] + 1, elf_location[1] - 1)
            E = (elf_location[0] + 1, elf_location[1])
            SE = (elf_location[0] + 1, elf_location[1] + 1)
            S = (elf_location[0], elf_location[1] + 1)
            SW = (elf_location[0] - 1, elf_location[1] + 1)
            W = (elf_location[0] - 1, elf_location[1])
            NW = (elf_location[0] - 1, elf_location[1] - 1)

            # Check which of these direction we can move in
            moves_allowed = [not location in current_elf_locations for location in [N, NE, E, SE, S, SW, W, NW]]

            # Firstly, should this elf try to move at all (are all surrounfing squares empty)
            if all(moves_allowed):
                continue

            # If we should move, we then need to check which direction we can move in
            for i in range(4):
                if ((elf_direction + i) % 4) == 0 and (moves_allowed[0] and moves_allowed[1] and moves_allowed[7]):
                    elf["proposed_location"] = N
                    proposed_moves_counter[N] += 1
                    break
                elif ((elf_direction + i) % 4) == 1 and (moves_allowed[3] and moves_allowed[4] and moves_allowed[5]):
                    elf["proposed_location"] = S
                    proposed_moves_counter[S] += 1
                    break
                elif ((elf_direction + i) % 4) == 2 and (moves_allowed[5] and moves_allowed[6] and moves_allowed[7]):
                    elf["proposed_location"] = W
                    proposed_moves_counter[W] += 1
                    break
                elif ((elf_direction + i) % 4) == 3 and (moves_allowed[1] and moves_allowed[2] and moves_allowed[3]):
                    elf["proposed_location"] = E
                    proposed_moves_counter[E] += 1
                    break

        # Now check if the elves can make the moves they proposed
        if len(proposed_moves_counter) != 0:
            for elf in elves:
                current_location = elf["current_location"]
                proposed_location = elf["proposed_location"]
                if proposed_location != current_location and proposed_moves_counter[proposed_location] == 1:
                    current_elf_locations.remove(current_location)
                    elf["current_location"] = proposed_location
                    current_elf_locations.add(proposed_location)
                else:
                    elf["proposed_location"] = elf["current_location"]

        # Next round we'll rotate the order we look at the directions in (move the first to last)
        round_count += 1
        elf_direction = (elf_direction + 1) % 4

        if round_count % 100 == 0:
            print(round_count)  
        
        # If no elf wants to move, we're done
        if len(proposed_moves_counter) == 0:
            break

    print(round_count)        
    