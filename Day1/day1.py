from utils import read_input

def part1():
    input = read_input(1)

    sum = 0

    for line in input:

        # Determine the first integer in the line
        for char in line:
            if char.isdigit():
                first = int(char)
                break

        # Determine the last integer in the line
        for char in reversed(line):
            if char.isdigit():
                last = int(char)
                break

        # Determine the calibration value from the first and last numbers in the string

        cal_val = (first * 10) + last

        sum += cal_val

    print(sum)

def part2():
    input = read_input(1)

    word_num_map = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
                   }

    sum = 0

    for line in input:

        current_word = ""

        # Determine the first integer in the line
        for char in line:
            if char.isdigit():
                first = int(char)
                break
            else:
                current_word += char
                matches = [key for key in word_num_map if key in current_word]
                if any(matches):
                    first = word_num_map[matches[0]]
                    break

        current_word = ""

        # Determine the last integer in the line
        for char in reversed(line):
            if char.isdigit():
                last = int(char)
                break
            else:
                current_word += char
                matches = [key for key in word_num_map if ''.join(reversed(key)) in current_word]

                if any(matches):
                    last = word_num_map[matches[0]]
                    break

        # Determine the calibration value from the first and last numbers in the string

        cal_val = (first * 10) + last

        sum += cal_val

    print(sum)
