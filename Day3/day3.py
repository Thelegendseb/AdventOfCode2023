from utils import read_input

def part1():
    input_data = read_input(3)

    sum_parts = 0

    # 2D char array (y, x)
    engine_array = [list(line) for line in input_data]

    for y in range(len(engine_array)):

        line = engine_array[y]

        counting_num = False
        has_adjacent_symbol = False
        counted_num = ""

        for x in range(len(engine_array[y])):

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
                        sum_parts += int(counted_num)
                    counting_num = False
                    counted_num = ""

                # Reset the flag after processing a number
                has_adjacent_symbol = False

        if counting_num:
            if has_adjacent_symbol:
                sum_parts += int(counted_num)

    print(sum_parts)

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

