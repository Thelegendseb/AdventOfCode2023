from utils import read_input

def part1():
    input = read_input(2)

    sum = 0

    maxr = 12
    maxg = 13
    maxb = 14

    for line in input:

        r = g = b = 0

        game = line.split(': ')[1]
        rounds = game.split("; ")

        for i in range(len(rounds)):

            round = rounds[i]
            round_parts = round.split(", ")

            for j in range(len(round_parts)):

                turn = round_parts[j].split(" ")
                val = int(turn[0])
                if turn[1] == "red":
                    r = max(r, val)
                if turn[1] == "green":
                    g = max(g, val)
                if turn[1] == "blue":
                    b = max(b, val)

        if r <= maxr and g <= maxg and b <= maxb:
            gameid = line[line.find(' ') + 1: line.find(':')]
            sum += int(gameid)

    print(sum)

def part2():
    input = read_input(2)

    sum = 0

    for line in input:

        r = g = b = 0

        game = line.split(': ')[1]
        rounds = game.split("; ")

        for i in range(len(rounds)):

            round = rounds[i]
            round_parts = round.split(", ")

            for j in range(len(round_parts)):

                turn = round_parts[j].split(" ")
                val = int(turn[0])
                if turn[1] == "red":
                    r = max(r, val)
                if turn[1] == "green":
                    g = max(g, val)
                if turn[1] == "blue":
                    b = max(b, val)

        power = r * g * b
        print(power)
        sum += power

    print(sum)

