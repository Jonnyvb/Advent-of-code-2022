def Traverse_Map_Breadth(map, start_location, target_location):
    path_length = 0
    current_locations = [start_location]
    visited_locations = []
    end_found = False
    while not end_found:
        path_length += 1
        visited_locations.extend(current_locations)

        possible_locations = set()
        for location in current_locations:
            possible_locations.update(map[location]["can_visit"]) 

        possible_locations.difference_update(visited_locations)

        if target_location in possible_locations:
            return path_length
        elif len(possible_locations) == 0:
            return -1
        else:
            current_locations = possible_locations

if __name__ == "__main__":
    with open("Input.txt") as f:
        height_map = {}
        start_location = (0, 0)
        end_location = (0, 0)
        max_y = 0
        max_x = 0
        for y_coord, line in enumerate(f):
            line = line.strip()
            max_y = max(max_y, y_coord)
            for x_coord, char in enumerate(line):
                current_coord = (x_coord, y_coord)
                max_x = max(max_x, x_coord)
                height_map[current_coord] = {}
                if char == "S":
                    height_map[current_coord]["height"] = 0
                    start_location = current_coord
                elif char == "E":
                    height_map[current_coord]["height"] = 27
                    end_location = current_coord
                else:
                    height = ord(char) - 96
                    height_map[current_coord]["height"] = height

        print(f"Start: {start_location}")
        print(f"End: {end_location}")

        current_location = start_location
        visited_locations = set()
        visited_locations.add(current_location)

        # Check which direction we can move from each location
        for location, data in height_map.items():
            this_height = data["height"]
            location_up = (location[0], location[1] - 1)
            location_down = (location[0], location[1] + 1)
            location_left = (location[0] - 1, location[1])
            location_right = (location[0] + 1, location[1])
            data["can_visit"] = []

            if location_up[1] < 0 or not height_map[location_up]["height"] in range(this_height + 2):
                data["up"] = False
            else:
                data["up"] = True
                data["can_visit"].append(location_up)
                
            if location_down[1] > max_y or not height_map[location_down]["height"] in range(this_height + 2):
                data["down"] = False
            else:
                data["down"] = True
                data["can_visit"].append(location_down)

            if location_left[0] < 0 or not height_map[location_left]["height"] in range(this_height + 2):
                data["left"] = False
            else:
                data["left"] = True
                data["can_visit"].append(location_left)

            if location_right[0] > max_x or not height_map[location_right]["height"] in range(this_height + 2):
                data["right"] = False
            else:
                data["right"] = True
                data["can_visit"].append(location_right)

        path_length = Traverse_Map_Breadth(height_map, start_location, end_location)

        print(path_length)