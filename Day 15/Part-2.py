if __name__ == "__main__":
    with open("Input.txt") as f:
        boundary_level_top = 4000000
        #boundary_level_top = 20
        sensors = {}
        beacons = set()
        for line in f:
            line = line.strip()
            line_parts = line.replace("=", " ").replace(":", " ").replace(",", " ").split(" ")
            sensor_x = int(line_parts[3])
            sensor_y = int(line_parts[6])
            beacon_x = int(line_parts[13])
            beacon_y = int(line_parts[16])
            
            man_dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
            sensors[(sensor_x, sensor_y)] = man_dist
            beacons.add((beacon_x, beacon_y))

        possible_beacon_locations = []
        for y in range(boundary_level_top + 1):
            if y % 100000 == 0:
                print(y)
            # Evaluate which sensors we care about on this level
            this_level_sensors = {}
            impossible_x_ranges = []
            for sensor, dist in sensors.items():
                dist_to_y_level = abs(sensor[1] - y)
                if dist_to_y_level <= dist:
                    this_level_sensors[sensor] = dist
                    x_movement = dist - dist_to_y_level
                    min_x = max(sensor[0] - x_movement, 0)
                    max_x = min(sensor[0] + x_movement, boundary_level_top)
                    impossible_x_ranges.append((min_x, max_x))

            # Sort the ranges by their lower points and iterate through them
            # to determine if there's a gap in them
            impossible_x_ranges = sorted(impossible_x_ranges, key=lambda d: d[0])
            end_x = 0
            for i in range(len(impossible_x_ranges) - 1):
                # Account for the fact that the end of the total range might be
                # from the previous range still
                end_x = max(end_x, impossible_x_ranges[i][1])
                gap = impossible_x_ranges[i + 1][0] - end_x
                if gap > 1:
                    # If the gap is larger than 1, we don't have a continous range
                    x = end_x + 1
                    possible_beacon_locations.append((x, y))
                    break
                    
                end_x = max(end_x, impossible_x_ranges[i][1], impossible_x_ranges[i + 1][1])
            
            # If we've found the location, we can stop searching
            if len(possible_beacon_locations) > 0:
                break

        for location in possible_beacon_locations:
            print(location)
            tuning_frequency = (location[0] * 4000000) + location[1]
            print(tuning_frequency)
