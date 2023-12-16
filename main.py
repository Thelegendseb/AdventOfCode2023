import sys
import importlib

def run_part(day, part):
    try:
        module = importlib.import_module(f'Day{day}.day{day}')
        part_function = getattr(module, f'part{part}', None)

        if part_function:
            part_function()
        else:
            print(f"Part {part} not found for Day {day}.")
    except ModuleNotFoundError:
        print(f"Day {day} not found or not implemented yet.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <day> <part>")
        sys.exit(1)

    day_to_run = sys.argv[1]
    part_to_run = sys.argv[2]

    run_part(day_to_run, part_to_run)
