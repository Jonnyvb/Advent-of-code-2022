if __name__ == "__main__":
    with open("Input.txt") as f:
        # Coordinates as (x, y)
        head_coord = (0, 0)
        tail_coord = (0, 0)
        tail_visited_coords = set()
        tail_visited_coords.add(tail_coord)
        for line in f:
            line = line.replace("\n", "")
            direction, count = line.split(" ")

            for _ in range(int(count)):
                if direction == "U":
                    head_coord = (head_coord[0], head_coord[1] + 1)
                elif direction == "D":
                    head_coord = (head_coord[0], head_coord[1] - 1)
                elif direction == "R":
                    head_coord = (head_coord[0] + 1, head_coord[1])
                elif direction == "L":
                    head_coord = (head_coord[0] - 1, head_coord[1])

                x_diff = head_coord[0] - tail_coord[0]
                y_diff = head_coord[1] - tail_coord[1]

                # Default to not moving
                x_new_coord = tail_coord[0]
                y_new_coord = tail_coord[1]

                # Check if other coord needs to move too
                if abs(x_diff) > 1 :
                    y_new_coord = head_coord[1]
                elif abs(y_diff) > 1:
                    x_new_coord = head_coord[0]

                if x_diff > 1:
                    x_new_coord = tail_coord[0] + (x_diff - 1)
                elif x_diff < -1:
                    x_new_coord = tail_coord[0] + (x_diff + 1)
                elif y_diff > 1:
                    y_new_coord = tail_coord[1] + (y_diff - 1)
                elif y_diff < -1:
                    y_new_coord = tail_coord[1] + (y_diff + 1)

                tail_coord = (x_new_coord, y_new_coord)
                tail_visited_coords.add(tail_coord)
        
        print(len(tail_visited_coords))