def CompareLists(list_left, list_right):
    for index in range(min(len(list_left), len(list_right))):
        list_left_item = list_left[index]
        list_right_item = list_right[index]

        # if both items are lists, we need to compare the two sublists
        if isinstance(list_left_item, list) and isinstance(list_right_item, list):
            comp = CompareLists(list_left_item, list_right_item)
            if comp != 0:
                # if we have a definitive result, we can return it
                return comp

        # if both the items are digits, we can do a direct comparisson
        if isinstance(list_left_item, int) and isinstance(list_right_item, int):
            digit_left = int(list_left_item)
            digit_right = int(list_right_item)
            if digit_left < digit_right:
                return -1
            elif digit_left > digit_right:
                return 1
        elif isinstance(list_left_item, int):
            # otherwise one item is a list and the other a digit. Promot the digit to a list and compare them
            list_left_item = [list_left_item]
            comp = CompareLists(list_left_item, list_right_item)
            if comp != 0:
                return comp
        elif isinstance(list_right_item, int):
            list_right_item = [list_right_item]
            comp = CompareLists(list_left_item, list_right_item)
            if comp != 0:
                return comp
    
    # If we get to the end of a list, check which lits was longer
    if len(list_left) < len(list_right):
        return -1
    elif len(list_left) > len(list_right):
        return 1
    else:
        return 0        

if __name__ == "__main__":
    with open("Input.txt") as f:
        packet_pairs = []
        packet_index = 0
        for line in f:
            line = line.strip()
            
            if packet_index == 0:
                packet_pairs.append([])
            
            if packet_index < 2:
                packet_pairs[len(packet_pairs) - 1].append(eval(line))
            
            packet_index += 1

            if packet_index >= 3:
                packet_index = 0

        packet_index_total = 0
        for packet_index, packet_pair in enumerate(packet_pairs):
            comp = CompareLists(packet_pair[0], packet_pair[1])
            if comp < 0:
                packet_index_total += (packet_index + 1)

        print(packet_index_total)
