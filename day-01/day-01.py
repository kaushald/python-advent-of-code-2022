def read_file(param):
    with open(param, 'r') as f:
        return f.read()


if __name__ == '__main__':
    lines = read_file('day-01/day-01-input.txt')

    current_elf_calories = 0
    top_1_calories = 0
    top_2_calories = 0
    top_3_calories = 0

    for line in lines.splitlines():
        if line == '':
            if current_elf_calories >= top_3_calories:
                if current_elf_calories >= top_2_calories:
                    if current_elf_calories >= top_1_calories:
                        top_3_calories = top_2_calories
                        top_2_calories = top_1_calories
                        top_1_calories = current_elf_calories
                    else:
                        top_3_calories = top_2_calories
                        top_2_calories = current_elf_calories
                else:
                    top_3_calories = current_elf_calories

            current_elf_calories = 0

        else:
            current_elf_calories = current_elf_calories + int(line)

    print("Top 3 values of heap : " + str(top_1_calories) + " " + str(top_2_calories) + " " + str(top_3_calories))
    print("Sum of top 3 values of heap : " + str(top_1_calories + top_2_calories + top_3_calories))
