def load_data(filepath):
    try:
        with open(filepath, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
            return lines

    except FileNotFoundError:
        print("File not found!")
        return None