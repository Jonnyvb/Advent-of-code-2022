from functools import cmp_to_key

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
        packets = []
        packets.append([[2]])
        packets.append([[6]])
        for line in f:
            line = line.strip()
            if not line == "":
                packets.append(eval(line))

        packets.sort(key=cmp_to_key(CompareLists))

        decoder_key_1 = packets.index([[2]]) + 1
        decoder_key_2 = packets.index([[6]]) + 1
        decoder_key = decoder_key_1 * decoder_key_2

        print(decoder_key)
