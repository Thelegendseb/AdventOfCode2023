import sys
import importlib

def run_day(day):
    try:
        module = importlib.import_module(f'Day{day}.day{day}')
        # Run the module without calling a specific function
        return module
    except ModuleNotFoundError:
        print(f"Day {day} not found or not implemented yet.")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <day>")
    else:
        day_to_run = sys.argv[1]
        module = run_day(day_to_run)
        # if module:
        #     print(f"Running day {day_to_run}")
        #     # This will execute the module's code without calling a specific function
