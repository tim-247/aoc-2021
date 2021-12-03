from collections import Counter

def lines_to_columns(lines: list) -> list:

    return [ [ int(line[index]) for line in lines ] for index, char in enumerate(lines[0]) ]

def get_most_common(column: list, default: str, least_common:bool = False) -> str:

    data = Counter(column)

    if data[0] == data[1]:
        return default
    elif not least_common:
        return data.most_common(1)[0][0]
    elif least_common:
        return data.most_common(2)[1][0]


def part1(lines: list) -> None:

    columns = lines_to_columns(lines)
    
    gamma_str = ''
    epsilon_str = ''

    for column in columns:
        if sum(column) > len(column) - sum(column):
            gamma_str += '1'
            epsilon_str += '0'
        else:
            gamma_str += '0'
            epsilon_str += '1'
    
    print(f"Gamma: {int(gamma_str,2)}, Epsilon: {int(epsilon_str, 2)}")
    print(f"Power: {int(gamma_str, 2) * int(epsilon_str, 2)}")

    # return gamma_str[0]
     

def part2(lines: list) -> None:

    o2_input = [ line for line in lines ]
    co2_input = [ line for line in lines ]

    print("Processing O2")

    for index, char in enumerate(o2_input[0]):
        most_common = get_most_common(lines_to_columns(o2_input)[index], '1')
        o2_input = [ line for line in o2_input if str(line[index]) == str(most_common) ]
        if len(o2_input) == 2:
            o2_input = [ line for line in o2_input if line[index+1] == '1' ]
            print(f"Final O2: {o2_input}")
            break
        if len(o2_input) == 1:
            print(f"Final O2: {o2_input}")
            break

    print("Processing CO2")

    for index, char in enumerate(co2_input[0]):
        least_common = get_most_common(lines_to_columns(co2_input)[index], '0', True)
        co2_input = [ line for line in co2_input if str(line[index]) == str(least_common) ]
        if len(co2_input) == 2:
            co2_input = [ line for line in co2_input if line[index+1] == '0' ]
            print(f"Final CO2: {co2_input}")
            break
        if len(co2_input) == 1:
            print(f"Final CO2: {co2_input}")
            break

    print(o2_input, co2_input)
    print(int(o2_input[0], 2) * int(co2_input[0], 2))

if __name__ == "__main__":
    with open('day3/input.txt', 'r') as input:
        lines = [ line.rstrip() for line in input ]
    
    part1(lines)
    part2(lines)
