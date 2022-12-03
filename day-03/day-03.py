def read_file(param):
    with open(param, 'r') as f:
        return f.read()


# function to get ascii value of a character
def get_ascii_value(param):
    ascii_value = ord(param)
    if ascii_value < 96:
        return ascii_value - 65 + 27
    else:
        return ascii_value - 96


def puzzle_1(param):
    sum_of_priorities = 0

    for line in param.splitlines():
        first_half_content = line[:len(line) // 2]
        second_half_content = line[len(line) // 2:]

        first_half_set = set(first_half_content)
        second_half_set = set(second_half_content)

        intersection = first_half_set.intersection(second_half_set)

        sum_of_priorities = sum_of_priorities + get_ascii_value(list(intersection)[0])

    print(sum_of_priorities)


def puzzle_2(param):
    sum_of_priorities = 0
    three_counter = 0

    last_line = ''
    common_characters = set()

    for line in param.splitlines():
        three_counter += 1
        if three_counter == 1:
            last_line = line
        elif three_counter == 2:
            common_characters = set(line) & set(last_line)
        elif three_counter == 3:
            badge = list(common_characters & set(line))[0]
            sum_of_priorities = sum_of_priorities + get_ascii_value(badge)
            three_counter = 0
    print(sum_of_priorities)


if __name__ == '__main__':
    lines = read_file("day-03/day-03-input.txt")
    puzzle_1(lines)
    puzzle_2(lines)
