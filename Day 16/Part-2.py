def Calculate_Distance_To_Valves(nodes, start_node, distances):
    depth = 0
    visited_nodes = set()
    visited_nodes.add(start_node)
    current_nodes = set()
    current_nodes.add(start_node)
    while len(visited_nodes) != len(nodes):
        next_nodes = set()
        for node in current_nodes:
            visited_nodes.add(node)
            distances[node] = depth + 1
            next_nodes.update(nodes[node]["leads_to"])
        
        current_nodes = next_nodes - visited_nodes
        depth += 1

def Calculate_Valve_Potential(distance, flow_rate, time_remaining):   
    if distance + 1 > time_remaining:
        # If the valve won't have any time to release pressure after we turn it on
        # it has no value to us
        return 0
    else:
        # Otherwise it has the potentially to run for the rest of the time, accounting
        # for actually getting to it, plus an additional minute to turn it on
        return (flow_rate * (time_remaining - distance))

def Explore_Graph(graph, my_valve, elephant_valve, my_time_to_move, elephant_time_to_move, time_remaining, cache):
    # If neither can move, we can just reduce our time down for everyone
    if my_time_to_move != 0 and elephant_time_to_move != 0:
        time_to_wait = min(my_time_to_move, elephant_time_to_move)
        my_time_to_move -= time_to_wait
        elephant_time_to_move -= time_to_wait
        time_remaining -= time_to_wait

    if time_remaining <= 0:
        return 0, []

    pressures = [0]
    vs = [[]]

    max_left_pressure = sum([max(graph[my_valve]["leads_to"][v][time_remaining - my_time_to_move], graph[elephant_valve]["leads_to"][v][time_remaining - elephant_time_to_move])  for v, data in graph.items() if not data["open"]])
    if max_left_pressure == 0:
        return 0, []

    valve_state = sum(1 << i for i, valve in enumerate(graph.items()) if valve[1]["open"])

    key1 = (valve_state, my_valve, elephant_valve, my_time_to_move, elephant_time_to_move, time_remaining)
    key2 = (valve_state, elephant_valve, my_valve, elephant_time_to_move, my_time_to_move, time_remaining)
    if key1 in cache: return cache[key1][0], cache[key1][1].copy()
    if key2 in cache: return cache[key2][0], cache[key2][1].copy()

    key = (valve_state, tuple(sorted([my_valve, elephant_valve])))
    if key in cache and cache[key][0] > max_left_pressure:
        return 0, []

    if my_time_to_move == 0:
        to_move = ["m", "e"]
    else:
        to_move = ["e"]

    for move in to_move:
        if move == "m":
            start_valve = my_valve 
        else:
            start_valve = elephant_valve
            if elephant_time_to_move > 0:
                time_to_wait = elephant_time_to_move
                my_time_to_move = max(0, my_time_to_move - time_to_wait)
                elephant_time_to_move -= time_to_wait
                time_remaining -= time_to_wait

        valves = {valve: graph[start_valve]["leads_to"][valve][time_remaining] for valve, data in graph.items() if not data["open"] and graph[start_valve]["leads_to"][valve][time_remaining] != 0}
        valves = dict(reversed(sorted(valves.items(), key=lambda item: item[1])))
        for valve, data in valves.items():
            distance_to_valve = graph[start_valve]["leads_to"][valve]["distance"]
            valve_potential = graph[start_valve]["leads_to"][valve][time_remaining]
            if valve_potential > 0:
                # Open the valve and explore the next level
                graph[valve]["open"] = True
                if move == "m":
                    pressure, v = Explore_Graph(graph, valve, elephant_valve, distance_to_valve, elephant_time_to_move, time_remaining, cache)
                else:
                    pressure, v = Explore_Graph(graph, my_valve, valve, my_time_to_move, distance_to_valve, time_remaining, cache)
                pressures.append(valve_potential + pressure)
                valve_open_time = time_remaining - distance_to_valve + 1
                v.append((valve, move, valve_open_time))
                vs.append(v)
                # Close this valve again so we can check the next route
                graph[valve]["open"] = False
        
        key = (valve_state, my_valve, elephant_valve, my_time_to_move, elephant_time_to_move, time_remaining)
        if key in cache:
            if cache[key][0] < max(pressures):
                cache[key] = (max(pressures), vs[pressures.index(max(pressures))].copy())
        else:
            cache[key] = (max(pressures), vs[pressures.index(max(pressures))].copy())

    key = (valve_state, tuple(sorted([my_valve, elephant_valve])))
    if key in cache:
        if cache[key][0] < max(pressures):
            cache[key] = (max(pressures), vs[pressures.index(max(pressures))].copy())
    else:
        cache[key] = (max(pressures), vs[pressures.index(max(pressures))].copy())

    return max(pressures), vs[pressures.index(max(pressures))].copy()

import time
if __name__ == "__main__":
    with open("Input.txt") as f:
        nodes = {}
        for line in f:
            line = line.strip().replace("=", " ").replace(";", "").replace(",", "")
            line = line.split(" ")
            valve = line[1]
            flow_rate = int(line[5])
            leads_to = line[10:]
            nodes[valve] = {"flow_rate": flow_rate, "leads_to": leads_to}

    reduced_graph = {}
    time_remaining = 26
    for node, node_info in nodes.items():
        # Flow rates of 0 are just paths, so we don't need them as a point in the graph
        # - they will just contibute to distances between points
        if node != "AA" and node_info["flow_rate"] == 0:
            continue

        reduced_graph[node] = {}
        reduced_graph[node]["flow_rate"] = node_info["flow_rate"]
        reduced_graph[node]["leads_to"] = {}
        reduced_graph[node]["open"] = False
        distances = {}
        Calculate_Distance_To_Valves(nodes, node, distances)
        for target_node, distance in distances.items():
            if node == target_node or (nodes[target_node]["flow_rate"] == 0 and target_node != "AA"):
                continue
            reduced_graph[node]["leads_to"][target_node] = {}   
            reduced_graph[node]["leads_to"][target_node]["distance"] = distance
            for time_left in range(time_remaining + 1):
                reduced_graph[node]["leads_to"][target_node][time_left] = Calculate_Valve_Potential(distance, nodes[target_node]["flow_rate"], time_left)

    reduced_graph["AA"]["open"] = True
    reduced_graph = dict(sorted(reduced_graph.items(), key=lambda item: item[1]["flow_rate"]))


    st = time.time()
    cache = {}
    released_pressure, route = Explore_Graph(reduced_graph, "AA", "AA", 0, 0, time_remaining, cache)
    et = time.time()
    elapsed_time = et - st

    route.reverse()
    print(route)
    print(released_pressure)
    print(f"Time taken: {elapsed_time}")