if __name__ == "__main__":
    with open("Input.txt") as f:
        test_y_level = 2000000
        sensors = {}
        beacons = set()
        min_x = 100000
        max_x = 0
        for line in f:
            line = line.strip()
            line_parts = line.replace("=", " ").replace(":", " ").replace(",", " ").split(" ")
            sensor_x = int(line_parts[3])
            sensor_y = int(line_parts[6])
            beacon_x = int(line_parts[13])
            beacon_y = int(line_parts[16])
            
            man_dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

            # If the straight line distance to the y level we care about is more
            # than the manhattan distance, we can just straight up ignore this sensor
            dist_to_y_level = abs(sensor_y - test_y_level)
            if dist_to_y_level <= man_dist:
                sensors[(sensor_x, sensor_y)] = man_dist
                beacons.add((beacon_x, beacon_y))
                x_movement = man_dist - dist_to_y_level
                min_x = min(min_x, sensor_x - x_movement)
                max_x = max(max_x, sensor_x + x_movement)

        print(f"Min x: {min_x}, max x: {max_x}")

        no_beacon_locations = []
        for x in range(min_x, max_x + 1):
            test_location_x = x
            test_location_y = test_y_level

            for sensor, dist in sensors.items():
                man_dist = abs(test_location_x - sensor[0]) + abs(test_location_y - sensor[1])
                if (man_dist <= dist 
                        and not (test_location_x, test_location_y) in beacons
                        and not (test_location_x, test_location_y) in sensors.keys()):
                    no_beacon_locations.append((test_location_x, test_location_y))
                    break

        print(len(no_beacon_locations))  

