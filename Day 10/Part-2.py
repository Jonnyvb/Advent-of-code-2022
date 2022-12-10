if __name__ == "__main__":
    with open("Input.txt") as f:
        register_value = 1
        cycle_number = 0
        reg_vals = [0]
        for line in f:
            line = line.replace("\n", "")

            if line.startswith("noop"):
                cycle_number += 1
                reg_vals.append(register_value)
            elif line.startswith("addx"):
                cycle_number += 2
                reg_vals.append(register_value)
                reg_vals.append(register_value)
                val = int(line.split(" ")[1])
                register_value += val

        screen_buffer = [[" " for x in range(40)] for y in range(6)]
        cycle = 0
        for y in range(6):
            for x in range(40):
                cycle += 1
                if x in range(reg_vals[cycle] - 1, reg_vals[cycle] + 2):
                    screen_buffer[y][x] = "#"
                else:
                    screen_buffer[y][x] = " "

        for line in screen_buffer:
            for char in line:
                print(char, end="")
            print("")