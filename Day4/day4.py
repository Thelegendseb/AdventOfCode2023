from utils import read_input

def part1():
    input = read_input(4)

    sum = 0

    for line in input:

        points = 0

        parts = line.split(" | ")
        winning_parts = parts[0].split(": ")
        winning_numbers_str = winning_parts[1]
        numbers_str = parts[1]

        numbers = list(map(int, filter(None, numbers_str.split(' '))))
        winning_numbers = list(map(int, filter(None, winning_numbers_str.split(' '))))

        for num in numbers:
            if num in winning_numbers:
                if points == 0:
                    points = 1
                else:
                    points *= 2

        sum += points

    print(sum)

def part2():
    input = read_input(4)

    copies = {}
    # card number: copy count

    for line in input:

        matches = 0

        parts = line.split(" | ")
        winning_parts = parts[0].split(": ")
        card_num = int(winning_parts[0].rsplit(' ', 1)[-1]) if winning_parts[0] else None
        winning_numbers_str = winning_parts[1]
        numbers_str = parts[1]

        numbers = list(map(int, filter(None, numbers_str.split(' '))))
        winning_numbers = list(map(int, filter(None, winning_numbers_str.split(' '))))

        if card_num in copies:
            copies[card_num] += 1
        else:
            copies[card_num] = 1

        for num in numbers:
            if num in winning_numbers:
                matches += 1

        for i in range(matches):
            key = i + 1 + card_num
            if key in copies:
                copies[key] += 1
            else:
                copies[key] = 1

        if copies[card_num] > 1:
            for c in range(copies[card_num] - 1):
                for i in range(matches):
                    key = i + 1 + card_num
                    if key in copies:
                        copies[key] += 1
                    else:
                        copies[key] = 1

    cardsum = sum(copies.values())

    print(cardsum)
