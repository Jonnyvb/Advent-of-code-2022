def snafu_to_decimal(snafu_number):
    decimal_version = 0
    position_value = 1
    for digit in reversed(snafu_number):
        if digit == "2":
            decimal_version += (position_value * 2)
        elif digit == "1":
            decimal_version += position_value
        elif digit == "-":
            decimal_version -= position_value
        elif digit == "=":
            decimal_version -= (position_value * 2)
    
        position_value *= 5

    return decimal_version

def decimlal_to_snafu(decimal_number):
    decimal_remaining = decimal_number
    position_value = 1
    highest_power_found = False
    max_positional_value = 0
    while not highest_power_found:
        max_positional_value += (2 * position_value)
        if decimal_number > max_positional_value:
            position_value *= 5
        else:
            highest_power_found = True

    snafu_number = []
    while position_value >= 1:
        if decimal_remaining > (1.5 * position_value):
            digit = "2"
            decimal_remaining -= (2 * position_value)
        elif decimal_remaining > (0.5 * position_value):
            digit = "1"
            decimal_remaining -= position_value
        elif decimal_remaining <= -(1.5 * position_value):
            digit = "="
            decimal_remaining += (2 * position_value)
        elif decimal_remaining <= -(0.5 * position_value):
            digit = "-"
            decimal_remaining += position_value
        else:
            digit = "0"

        snafu_number.append(digit)
        position_value /= 5

    return "".join(snafu_number)  

if __name__ == "__main__":
    snafu_numbers = []
    with open("Input.txt") as f:
        for line in f:
            line = line.strip()
            snafu_numbers.append(line)

    decimal_snafu_numbers = []
    for snafu_number in snafu_numbers:        
        decimal_snafu_numbers.append(snafu_to_decimal(snafu_number))
    
    total_decimal_fuel = sum(decimal_snafu_numbers)
    total_snafu_fuel = decimlal_to_snafu(total_decimal_fuel)

    print(total_snafu_fuel)