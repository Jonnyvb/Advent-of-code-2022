def Generate_Neighbour_Points(point):
    x = point[0]
    y = point[1]
    z = point[2]
    neighbour_points = []
    neighbour_points.append((x - 1, y, z))
    neighbour_points.append((x + 1, y, z))
    neighbour_points.append((x, y - 1, z))
    neighbour_points.append((x, y + 1, z))
    neighbour_points.append((x, y, z - 1))
    neighbour_points.append((x, y, z + 1))
    return neighbour_points

if __name__ == "__main__":
    with open("Input.txt") as f:
        points = set()
        max_x = 0
        max_y = 0
        max_z = 0
        for line in f:
            line = line.strip()
            # Shift coordinates by 1 to leave room for an airgap
            x, y, z = [int(n) + 1 for n in line.split(",")]
            points.add((x, y, z))
            # Add one to allow the airgap on the far side too
            max_x = max(max_x, x + 1)
            max_y = max(max_y, y + 1)
            max_z = max(max_z, z + 1)

    # Do a BFS to find all external air points around the lavaball
    external_air = set()
    # Start at (0, 0, 0) which we know is air as we fully enclosed the lavaball
    external_air.add((0, 0, 0))
    air_to_check = set()
    air_to_check.add((0, 0, 0))
    while len(air_to_check) > 0:
        new_external_air = set()
        for air_point in air_to_check:
            # Check all neighbour points
            points_to_check = Generate_Neighbour_Points(air_point)
            for point in points_to_check:
                # Check the point is within our bounding box
                if point[0] >= 0 and point[1] >= 0 and point[2] >= 0 and point[0] <= max_x and point[1] <= max_y and point[2] <= max_z:
                    # Check this point is air, and that we haven't already considered it
                    if not point in points and not point in external_air:
                        new_external_air.add(point)

        # Add these new points to all our known air, and mark the new parts as the next points to look from
        external_air = external_air.union(new_external_air)
        air_to_check = new_external_air

    # Check every magma point
    external_visible_faces = 0
    for point in points:
        point_visible_faces = 0
        # Check all the neighour points to see if that face is in the external air
        points_to_check = Generate_Neighbour_Points(point)
        for point_to_check in points_to_check:
            if point_to_check in external_air:
                point_visible_faces += 1
        external_visible_faces += point_visible_faces
    
    print(external_visible_faces)
