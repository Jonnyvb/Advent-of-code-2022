if __name__ == "__main__":
    monkeys = {}
    with open("Input.txt") as f:
        for i, line in enumerate(f):
            line = line.strip()
            monkey_name = line[:4]
            monkeys[monkey_name] = {}
            monkey_operation = line.split(": ")[1]
            if monkey_operation.isdigit():
                monkeys[monkey_name]["number"] = int(monkey_operation)
            else:
                sub_monkey_1 = monkey_operation.split(" ")[0]
                sub_op = monkey_operation.split(" ")[1]
                sub_monkey_2 = monkey_operation.split(" ")[2]
                monkeys[monkey_name]["op"] = [sub_monkey_1, sub_monkey_2, sub_op]
    
    root_monkey_solved = False
    while not root_monkey_solved:
        for monkey, action in monkeys.items():
            if not "number" in action:
                # We need to perform an operation, check if we have
                # numbers for both sub monkeys
                sub_monkey_1 = action["op"][0]
                sub_monkey_2 = action["op"][1]
                if "number" in monkeys[sub_monkey_1] and "number" in monkeys[sub_monkey_2]:
                    operation = action["op"][2]
                    if operation == "+":
                        action["number"] = monkeys[sub_monkey_1]["number"] + monkeys[sub_monkey_2]["number"]
                    elif operation == "-":
                        action["number"] = monkeys[sub_monkey_1]["number"] - monkeys[sub_monkey_2]["number"]
                    elif operation == "*":
                        action["number"] = monkeys[sub_monkey_1]["number"] * monkeys[sub_monkey_2]["number"]
                    elif operation == "/":
                        action["number"] = monkeys[sub_monkey_1]["number"] / monkeys[sub_monkey_2]["number"]

                    if monkey == "root":
                        root_monkey_solved = True

    print(int(monkeys["root"]["number"]))