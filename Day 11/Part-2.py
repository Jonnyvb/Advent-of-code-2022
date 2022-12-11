if __name__ == "__main__":
    with open("Input.txt") as f:
        current_monkey = 0
        monkeys = [{"items" : [], "operation": {"op" : "", "val": ""}, "test_div": 0, "true": 0, "false": 0, "inspected": 0} for x in range(8)]
        item_number = 0
        for line in f:
            line = line.strip()

            if line.startswith("Monkey"):
                line = line.strip(":")
                current_monkey = int(line.split(" ")[1])
            elif line.startswith("Starting"):
                items = line.replace(",", "").split(" ")[2:]
                for item in items:
                    monkeys[current_monkey]["items"].append((item_number, int(item)))
                    item_number += 1
            elif line.startswith("Operation"):
                monkeys[current_monkey]["operation"]["op"] = line.split(" ")[4]
                monkeys[current_monkey]["operation"]["val"] = line.split(" ")[5]
            elif line.startswith("Test"):
                monkeys[current_monkey]["test_div"] = int(line.split(" ")[3])
            elif line.startswith("If true"):
                monkeys[current_monkey]["true"] = int(line.split(" ")[-1])
            elif line.startswith("If false"):
                monkeys[current_monkey]["false"] = int(line.split(" ")[-1])

        divisors = set([monkey["test_div"] for monkey in monkeys])
        print(divisors)
        common_divisor = 1
        for divisor in divisors:
            if divisor != 0:
                common_divisor *= divisor

        round = 0
        while round < 10000:
            print(f"Starting round {round}")
            for monkey in monkeys:
                while len(monkey["items"]) != 0:
                    # Take first item
                    item = monkey["items"].pop(0)

                    # Look at its current worry level
                    worry_level = item[1]

                    # Monkey inspects it
                    monkey["inspected"] += 1
                    if monkey["operation"]["val"] == "old":
                        op_value = worry_level
                    else:
                        op_value = int(monkey["operation"]["val"])
                    
                    op = monkey["operation"]["op"]
                    if op == "+":
                        worry_level += op_value
                    elif op == "*":
                        worry_level *= op_value

                    worry_level = worry_level % common_divisor

                    # Construct new item for new worry level, with same index
                    item = (item[0], worry_level)

                    # Apply the monkeys test
                    if worry_level % monkey["test_div"] == 0:
                        monkeys[monkey["true"]]["items"].append(item)
                    else:
                        monkeys[monkey["false"]]["items"].append(item)

            round += 1

        inspected_counts = [monkey["inspected"] for monkey in monkeys]
        inspected_counts.sort()
        print(inspected_counts)

        monkey_business = inspected_counts[-1] * inspected_counts[-2]
        print(monkey_business)
