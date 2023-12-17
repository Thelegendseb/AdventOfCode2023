from utils import read_input

def part1():
    input_data = read_input(3)

    sum = 0

    # 2D char array (y, x)
    engine_array = [list(line) for line in input_data]

    for y in range(len(engine_array)):

        line = engine_array[y]

        counting_num = False
        has_adjacent_symbol = False
        counted_num = ""

        for x in range(len(line)):

            element = line[x]

            if element.isdigit():
                counted_num += element
                if not counting_num:
                    counting_num = True

                if is_adjacent_to_symbol(y, x, engine_array):
                    has_adjacent_symbol = True

            else:
                if counting_num:
                    if has_adjacent_symbol:
                        sum += int(counted_num)
                    counting_num = False
                    counted_num = ""

                # Reset the flag after processing a number
                has_adjacent_symbol = False

        if counting_num:
            if has_adjacent_symbol:
                sum += int(counted_num)

    print(sum)

def part2():
    input_data = read_input(3)

    sum = 0

    # 2D char array (y, x)
    engine_array = [list(line) for line in input_data]

    asterisk_dict = {}

    for y in range(len(engine_array)):

        line = engine_array[y]

        counting_num = False
        counted_num = ""

        temp_asterisks = []

        for x in range(len(line)):

            element = line[x]

            if element.isdigit():
                counted_num += element
                if not counting_num:
                    counting_num = True

                pos_res = get_adjacent_asterisk_positions(y,x,engine_array)
                for pos in pos_res:
                    temp_asterisks.append(pos)

            else:
                if counting_num:
                    full_num = int(counted_num)
                    temp_asterisks = list(set(temp_asterisks))
                    for asterisk_pos in temp_asterisks:
                        if asterisk_pos in asterisk_dict:
                            asterisk_dict[asterisk_pos].append(full_num)
                        else:
                            asterisk_dict[asterisk_pos] = [full_num]
                    counting_num = False
                    counted_num = ""
                    temp_asterisks = []

        if counting_num:
            full_num = int(counted_num)
            temp_asterisks = list(set(temp_asterisks))
            for asterisk_pos in temp_asterisks:
                if asterisk_pos in asterisk_dict:
                    asterisk_dict[asterisk_pos].append(full_num)
                else:
                    asterisk_dict[asterisk_pos] = [full_num]

    for pos, neighbors in asterisk_dict.items():
        if len(neighbors) == 2:
            product = neighbors[0] * neighbors[1]
            sum += product

    print(sum)

def get_adjacent_asterisk_positions(y, x, engine_array):
    positions = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            new_y, new_x = y + i, x + j

            if 0 <= new_y < len(engine_array) and 0 <= new_x < len(engine_array[y]):
                if engine_array[new_y][new_x] == '*':
                    positions.append((new_y, new_x))

    return positions


def is_adjacent_to_symbol(y, x, engine_array):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            new_y, new_x = y + i, x + j

            if 0 <= new_y < len(engine_array) and 0 <= new_x < len(engine_array[y]):
                if engine_array[new_y][new_x] not in {'.'} and not engine_array[new_y][new_x].isdigit():
                    return True

    return False

