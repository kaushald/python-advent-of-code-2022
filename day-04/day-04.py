from utils.file import read_file


def read_numbers(param):
    split_pairs = param.split(',')
    ranges = {'l1': split_pairs[0].split('-')[0], 'l2': split_pairs[0].split('-')[1],
              'r1': split_pairs[1].split('-')[0], 'r2': split_pairs[1].split('-')[1]}
    return ranges


def puzzle_1(param):
    full_overlap = 0
    for line in param.splitlines():
        ranges = read_numbers(line)

        range_1_size = int(ranges['l2']) - int(ranges['l1'])
        range_2_size = int(ranges['r2']) - int(ranges['r1'])
        if range_1_size > range_2_size:
            if int(ranges['l1']) <= int(ranges['r1']) and int(ranges['l2']) >= int(ranges['r2']):
                full_overlap += 1

        else:
            if int(ranges['r1']) <= int(ranges['l1']) and int(ranges['r2']) >= int(ranges['l2']):
                full_overlap += 1

    print('Full Overlaps:', full_overlap)


def puzzle_2(param):
    partial_overlap = 0
    for line in param.splitlines():
        ranges = read_numbers(line)

        if int(ranges['l1']) <= int(ranges['r1']) <= int(ranges['l2']):
            partial_overlap += 1

        elif int(ranges['r1']) <= int(ranges['l1']) <= int(ranges['r2']):
            partial_overlap += 1

    print('Partial Overlaps:', partial_overlap)


if __name__ == '__main__':
    lines = read_file("day-04/day-04-input.txt")
    puzzle_1(lines)
    puzzle_2(lines)
