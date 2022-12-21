if __name__ == "__main__":
    monkeys = {}
    with open("Input.txt") as f:
        for i, line in enumerate(f):
            line = line.strip()
            monkey_name = line[:4]
            monkeys[monkey_name] = {}
            monkey_operation = line.split(": ")[1]
            if monkey_name != "humn":
                if monkey_operation.isdigit():
                    monkeys[monkey_name]["number"] = int(monkey_operation)
                else:
                    sub_monkey_1 = monkey_operation.split(" ")[0]
                    sub_op = monkey_operation.split(" ")[1]
                    sub_monkey_2 = monkey_operation.split(" ")[2]
                    monkeys[monkey_name]["op"] = [sub_monkey_1, sub_monkey_2, sub_op]

    # Solve as many of the monkeys as we can
    all_monkeys_solved = False
    while not all_monkeys_solved:
        all_monkeys_solved = True
        for monkey, action in monkeys.items():
            if monkey == "humn": continue

            if not "number" in action:
                # We need to perform an operation, check if we have
                # numbers for both sub monkeys
                sub_monkey_1 = action["op"][0]
                sub_monkey_2 = action["op"][1]

                # If one of the submonkeys is us, we can't expand as we don't know our number
                if sub_monkey_1 == "humn" or sub_monkey_2 == "humn": continue

                if "number" in monkeys[sub_monkey_1] and "number" in monkeys[sub_monkey_2]:
                    all_monkeys_solved = False
                    operation = action["op"][2]
                    if operation == "+":
                        action["number"] = monkeys[sub_monkey_1]["number"] + monkeys[sub_monkey_2]["number"]
                    elif operation == "-":
                        action["number"] = monkeys[sub_monkey_1]["number"] - monkeys[sub_monkey_2]["number"]
                    elif operation == "*":
                        action["number"] = monkeys[sub_monkey_1]["number"] * monkeys[sub_monkey_2]["number"]
                    elif operation == "/":
                        action["number"] = monkeys[sub_monkey_1]["number"] / monkeys[sub_monkey_2]["number"]

    
    # Try solving both sides of the root monkey. If we can solve one side, we can
    # work backwards on the other side

    lhs_monkey = monkeys["root"]["op"][0]
    rhs_monkey = monkeys["root"]["op"][1]

    if not "number" in monkeys[lhs_monkey]:
        monkey_to_expand = lhs_monkey
        result_should_be = monkeys[rhs_monkey]["number"]
    else:
        monkey_to_expand = rhs_monkey
        result_should_be = monkeys[lhs_monkey]["number"]

    while not "number" in monkeys["humn"]:
        sub_monkey_1 = monkeys[monkey_to_expand]["op"][0]
        sub_monkey_2 = monkeys[monkey_to_expand]["op"][1]
        operation = monkeys[monkey_to_expand]["op"][2]

        # One of these should have a number, then we'll expand the other one
        if "number" in monkeys[sub_monkey_1]:
            if operation == "+":
                result_should_be = result_should_be - monkeys[sub_monkey_1]["number"]
            elif operation == "-":
                result_should_be = monkeys[sub_monkey_1]["number"] - result_should_be
            elif operation == "*":
                result_should_be = result_should_be / monkeys[sub_monkey_1]["number"]
            elif operation == "/":
                result_should_be = monkeys[sub_monkey_1]["number"] / result_should_be

            monkeys[sub_monkey_2]["number"] = result_should_be
            monkey_to_expand = sub_monkey_2
        else:
            if operation == "+":
                result_should_be = result_should_be - monkeys[sub_monkey_2]["number"]
            elif operation == "-":
                result_should_be = monkeys[sub_monkey_2]["number"] + result_should_be
            elif operation == "*":
                result_should_be = result_should_be / monkeys[sub_monkey_2]["number"]
            elif operation == "/":
                result_should_be = monkeys[sub_monkey_2]["number"] * result_should_be

            monkeys[sub_monkey_1]["number"] = result_should_be
            monkey_to_expand = sub_monkey_1

    print(int(monkeys["humn"]["number"]))