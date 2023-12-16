import os

def read_input(day):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, f"Day{day}", "input.txt")

    try:
        with open(input_file_path, "r") as file:
            input_data = file.read()
            return input_data
    except FileNotFoundError:
        print(f"Input file for Day {day} not found.")
        return None