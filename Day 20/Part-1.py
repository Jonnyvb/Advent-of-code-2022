if __name__ == "__main__":
    coordinates = []
    with open("Input.txt") as f:
        for i, line in enumerate(f):
            line = line.strip()
            coordinates.append((i, int(line)))

    for i in range(len(coordinates)):
        current_location = next(index for index, coord in enumerate(coordinates) if coord[0] == i)
        coord = coordinates.pop(current_location)
        shift = coord[1]
        new_location = (current_location + shift) % len(coordinates)
        if new_location == 0: new_location += len(coordinates)
        coordinates.insert(new_location, coord)

    zero_position = next(index for index, coord in enumerate(coordinates) if coord[1] == 0)
    positions_to_check = [1000, 2000, 3000]
    coordinate_sum = 0
    for position in positions_to_check:
        coordinate_sum += coordinates[(position + zero_position) % len(coordinates)][1]

    print(coordinate_sum)