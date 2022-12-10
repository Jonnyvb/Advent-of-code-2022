if __name__ == "__main__":
    with open("Input.txt") as f:
        register_value = 1
        cycle_number = 0
        signal_strengths = [0]
        for line in f:
            line = line.replace("\n", "")

            if line.startswith("noop"):
                cycle_number += 1
                signal_strengths.append(cycle_number * register_value)
            elif line.startswith("addx"):
                cycle_number += 1
                signal_strengths.append(cycle_number * register_value)
                cycle_number += 1
                signal_strengths.append(cycle_number * register_value)
                val = int(line.split(" ")[1])
                register_value += val

        signal_strength_sum = 0
        for i, signal_strength in enumerate(signal_strengths[20::40]):
            print(f"{i} : {signal_strength}")
            signal_strength_sum += signal_strength

        print(signal_strength_sum)