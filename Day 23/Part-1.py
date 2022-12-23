def Print_Elf_Locations(elves):
    current_elf_locations = [elf["current_location"] for elf in elves]
    min_x = min([elf["current_location"][0] for elf in elves])
    max_x = max([elf["current_location"][0] for elf in elves])
    min_y = min([elf["current_location"][1] for elf in elves])
    max_y = max([elf["current_location"][1] for elf in elves])

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in current_elf_locations:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()

if __name__ == "__main__":
    elves = []
    with open("Input.txt") as f:
        for i, line in enumerate(f):
            for j, char in enumerate(line):
                if char == "#":
                     # Sotre next direction, 0 for N, 1 for S, 2 for W, 3 for E
                     # followed by the elf's next proposed move
                    elves.append({"current_location": (j, i), "proposed_location": (j, i)})

    elf_direction = 0

    # The elves want to do 10 round
    for _ in range(10):
        # Find all the proposed elf moves
        proposed_moves = []
        current_elf_locations = [elf["current_location"] for elf in elves]
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

            # Firstly, should this elf try to move at all (are all surrounfing squares empty)
            if not any(location in current_elf_locations for location in [N, NE, E, SE, S, SW, W, NW]):
                continue

            # If we should move, we then need to check which direction we can move in
            for i in range(4):
                if ((elf_direction + i) % 4) == 0 and not any(location in current_elf_locations for location in [N, NE, NW]):
                    elf["proposed_location"] = N
                    proposed_moves.append(N)
                    break
                elif ((elf_direction + i) % 4) == 1 and not any(location in current_elf_locations for location in [S, SE, SW]):
                    elf["proposed_location"] = S
                    proposed_moves.append(S)
                    break
                elif ((elf_direction + i) % 4) == 2 and not any(location in current_elf_locations for location in [W, NW, SW]):
                    elf["proposed_location"] = W
                    proposed_moves.append(W)
                    break
                elif ((elf_direction + i) % 4) == 3 and not any(location in current_elf_locations for location in [E, NE, SE]):
                    elf["proposed_location"] = E
                    proposed_moves.append(E)
                    break
        
        # If no elf wants to move, we're done
        if len(proposed_moves) == 0:
            break

        # Now check if the elves can make the moves they proposed
        for elf in elves:
            current_location = elf["current_location"]
            proposed_location = elf["proposed_location"]
            if proposed_location != current_location:
                proposed_move_count = proposed_moves.count(proposed_location)
                if proposed_move_count == 1:
                    elf["current_location"] = proposed_location

        # Next round we'll rotate the order we look at the directions in (move the first to last)
        elf_direction = (elf_direction + 1) % 4

    current_elf_locations = [elf["current_location"] for elf in elves]
    min_x = min([elf["current_location"][0] for elf in elves])
    max_x = max([elf["current_location"][0] for elf in elves])
    min_y = min([elf["current_location"][1] for elf in elves])
    max_y = max([elf["current_location"][1] for elf in elves])

    rectangle_area = (max_x - min_x + 1) * (max_y - min_y + 1)
    empty_square_count = rectangle_area - len(elves)

    print(empty_square_count)        
    