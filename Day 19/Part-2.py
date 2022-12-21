def Recurse_Mine(blueprint, previous_possible_builds, time_remaining):
    # If there's no time left, return how much obsidian we mined
    if time_remaining == 1:
        return blueprint["geode"] + blueprint["geode_robot_count"], ["wait it out", time_remaining, (blueprint["ore"], blueprint["clay"], blueprint["obsidian"], blueprint["geode"])]

    # Check which robots we could build
    builds_available = []

    # If we don't have time to build any more geode robots, we won't do anything
    #maximum_left_obsidian = blueprint["obsidian"] + (((time_remaining) * (time_remaining - 1)) / 2) + (time_remaining * blueprint["obsidian_robot_count"])
#
    #if maximum_left_obsidian <= blueprint["geode_robot_cost"][1]:
    #    return blueprint["geode"] + blueprint["geode_robot_count"], [("wait it out", time_remaining)]
    #else:
    if blueprint["ore"] >= blueprint["geode_robot_cost"][0] and blueprint["obsidian"] >= blueprint["geode_robot_cost"][1]:
        if not "build_geode_robot" in previous_possible_builds: builds_available.append("build_geode_robot")
    else:
        if blueprint["ore"] >= blueprint["obsidian_robot_cost"][0] and blueprint["clay"] >= blueprint["obsidian_robot_cost"][1]:
            if blueprint["obsidian_robot_count"] < blueprint["max_obsidian_needed_per_turn"]:
                if not "build_obsidian_robot" in previous_possible_builds: builds_available.append("build_obsidian_robot")
        if blueprint["ore"] >= blueprint["ore_robot_cost"]:
            if blueprint["ore_robot_count"] < blueprint["max_ore_needed_per_turn"]:
                if not "build_ore_robot" in previous_possible_builds: builds_available.append("build_ore_robot")
        if blueprint["ore"] >= blueprint["clay_robot_cost"]:
            if blueprint["clay_robot_count"] < blueprint["max_clay_needed_per_turn"]:
                if not "build_clay_robot" in previous_possible_builds: builds_available.append("build_clay_robot")        

        # When should we try waiting?
        if (blueprint["ore"] < blueprint["clay_robot_cost"]
            or blueprint["ore"] < blueprint["ore_robot_cost"]
            or blueprint["clay"] < blueprint["obsidian_robot_cost"][1] and blueprint["clay_robot_count"] > 0
            or blueprint["obsidian"] < blueprint["geode_robot_cost"][1] and blueprint["obsidian_robot_count"] > 0):
            builds_available.insert(0, "none")

    # Mine our resource
    blueprint["ore"] += blueprint["ore_robot_count"]
    blueprint["clay"] += blueprint["clay_robot_count"]
    blueprint["obsidian"] += blueprint["obsidian_robot_count"]
    blueprint["geode"] += blueprint["geode_robot_count"]

    # We can only build one robot a round, so try building each and see what happens
    # This includes the action of not building anything
    most_geodes = -1
    best_actions = []
    for build in builds_available:
        if build == "build_ore_robot":
            blueprint["ore"] -= blueprint["ore_robot_cost"]
            blueprint["ore_robot_count"] += 1
        elif build == "build_clay_robot":
            blueprint["ore"] -= blueprint["clay_robot_cost"]
            blueprint["clay_robot_count"] += 1
        elif build == "build_obsidian_robot":
            blueprint["ore"] -= blueprint["obsidian_robot_cost"][0]
            blueprint["clay"] -= blueprint["obsidian_robot_cost"][1]
            blueprint["obsidian_robot_count"] += 1
        elif build == "build_geode_robot":
            blueprint["ore"] -= blueprint["geode_robot_cost"][0]
            blueprint["obsidian"] -= blueprint["geode_robot_cost"][1]
            blueprint["geode_robot_count"] += 1
        else:
            pass

        if build == "none":
            mined_geodes, action = Recurse_Mine(blueprint, builds_available, time_remaining - 1)
        else:
            mined_geodes, action = Recurse_Mine(blueprint, [], time_remaining - 1)
        if mined_geodes > most_geodes:
            most_geodes = mined_geodes
            action.append((build, time_remaining, (blueprint["ore"], blueprint["clay"], blueprint["obsidian"], blueprint["geode"])))
            best_actions = action.copy()
        
        # Undo our build so we can try the next action
        if build == "build_ore_robot":
            blueprint["ore"] += blueprint["ore_robot_cost"]
            blueprint["ore_robot_count"] -= 1
        if build == "build_clay_robot":
            blueprint["ore"] += blueprint["clay_robot_cost"]
            blueprint["clay_robot_count"] -= 1
        if build == "build_obsidian_robot":
            blueprint["ore"] += blueprint["obsidian_robot_cost"][0]
            blueprint["clay"] += blueprint["obsidian_robot_cost"][1]
            blueprint["obsidian_robot_count"] -= 1
        if build == "build_geode_robot":
            blueprint["ore"] += blueprint["geode_robot_cost"][0]
            blueprint["obsidian"] += blueprint["geode_robot_cost"][1]
            blueprint["geode_robot_count"] -= 1

    # Un-mine our resource so we can recurse back up
    blueprint["ore"] -= blueprint["ore_robot_count"]
    blueprint["clay"] -= blueprint["clay_robot_count"]
    blueprint["obsidian"] -= blueprint["obsidian_robot_count"]
    blueprint["geode"] -= blueprint["geode_robot_count"]

    return most_geodes, best_actions

if __name__ == "__main__":
    blueprints = []
    with open("TestInput.txt") as f:
        for i, line in enumerate(f):
            if i == 3: break
            line = line.strip().replace(":", "")
            nums = [int(num) for num in line.split(" ") if num.isdigit()]
            blueprint = {}
            blueprint["ID"] = nums[0]
            blueprint["ore_robot_count"] = 1
            blueprint["clay_robot_count"] = 0
            blueprint["obsidian_robot_count"] = 0
            blueprint["geode_robot_count"] = 0            
            blueprint["ore_robot_cost"] = nums[1]
            blueprint["clay_robot_cost"] = nums[2]
            blueprint["obsidian_robot_cost"] = (nums[3], nums[4])
            blueprint["geode_robot_cost"] = (nums[5], nums[6])
            blueprint["ore"] = 0
            blueprint["clay"] = 0
            blueprint["obsidian"] = 0
            blueprint["geode"] = 0
            blueprint["max_ore_needed_per_turn"] = max(nums[1], nums[2], nums[3], nums[5])
            blueprint["max_clay_needed_per_turn"] = nums[4]
            blueprint["max_obsidian_needed_per_turn"] = nums[6]
            blueprints.append(blueprint)

    geode_product = 1
    for blueprint in blueprints:
        time_to_run = 32
        mined_geodes, actions = Recurse_Mine(blueprint, [], time_to_run)
        print(f"ID {blueprint['ID']} Mined {mined_geodes}")
        for action in reversed(actions):
            print(33 - action[1], action[0], action[2])
        geode_product *= mined_geodes

    print(geode_product)