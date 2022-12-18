if __name__ == "__main__":
    with open("Input.txt") as f:
        points = set()
        max_x = 0
        max_y = 0
        max_z = 0
        for line in f:
            line = line.strip()
            x, y, z = [int(n) for n in line.split(",")]
            points.add((x, y, z))

    visible_faces = 0
    for point in points:
        x = point[0]
        y = point[1]
        z = point[2]
        point_visible_faces = 0
        if not (x - 1, y, z) in points : point_visible_faces += 1
        if not (x + 1, y, z) in points : point_visible_faces += 1
        if not (x, y - 1, z) in points : point_visible_faces += 1
        if not (x, y + 1, z) in points : point_visible_faces += 1
        if not (x, y, z - 1) in points : point_visible_faces += 1
        if not (x, y, z + 1) in points : point_visible_faces += 1
        visible_faces += point_visible_faces
    
    print(visible_faces)
