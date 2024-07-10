import sys
import os

def parsowanie():
    if len(sys.argv) != 3:
        print("Jak używać: program.exe plik1.x plik2.y")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    input_format = os.path.splitext(input_file)[1]
    output_format = os.path.splitext(output_file)[1]

    if input_format not in ['.xml', '.json', '.yml', '.yaml'] or output_format not in ['.xml', '.json', '.yml', '.yaml']:
        print("Obsługiwane są tylko formaty: .xml, .json, .yml, .yaml")
        sys.exit(1)

    return input_file, output_file, input_format, output_format

if __name__ == "__main__":
    input_file, output_file, input_format, output_format = parsowanie()