import sys
import os
import json

def parsowanie():
    if len(sys.argv) != 3:
        print("Jak używać: program.exe pathFile1.x patchFile2.y")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    input_format = os.path.splitext(input_file)[1]
    output_format = os.path.splitext(output_file)[1]

    if input_format not in ['.xml', '.json', '.yml', '.yaml'] or output_format not in ['.xml', '.json', '.yml', '.yaml']:
        print("Obsługiwane są tylko formaty: .xml, .json, .yml, .yaml")
        sys.exit(1)

    return input_file, output_file, input_format, output_format

def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Nie znaleziono pliku: {file_path}")
        sys.exit(1)

if __name__ == "__main__":
    input_file, output_file, input_format, output_format = parsowanie()
    if input_format == '.json':
        data = read_json(input_file)