import sys
import os
import json
import xml.etree.ElementTree as ET
import yaml
import xml

def parsowanie():
    if len(sys.argv) != 3:
        print("Jak używać: program.exe pathFile1.x pathFile2.y")
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
        print(f"Error dekodowania JSON: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Nie znaleziono pliku: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def write_json(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def read_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except ET.ParseError as e:
        print(f"Error parsowania XML: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Nie znaleziono pliku: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def write_xml(data, file_path):
    try:
        tree = ET.ElementTree(data)
        tree.write(file_path)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def read_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data
    except yaml.YAMLError as e:
        print(f"Error parsowania YAML: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Nie znaleziono pliku: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def write_yaml(data, file_path):
    try:
        with open(file_path, 'w') as file:
            yaml.dump(data, file)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def convert_data(data, output_format):
    if output_format in ['.json', '.xml', '.yml', '.yaml']:
        return data
    else:
        print("Unsupported format")
        sys.exit(1)

if __name__ == "__main__":
    input_file, output_file, input_format, output_format = parsowanie()

    if input_format == '.json':
        data = read_json(input_file)
    elif input_format == '.xml':
        data = read_xml(input_file)
    elif input_format in ['.yml', '.yaml']:
        data = read_yaml(input_file)
    else:
        print("Zły format")
        sys.exit(1)

    converted_data = convert_data(data, output_format)

    if output_format == '.json':
        write_json(converted_data, output_file)
    elif output_format == '.xml':
        write_xml(converted_data, output_file)
    elif output_format in ['.yml', '.yaml']:
        write_yaml(converted_data, output_file)
    else:
        print("Zły format")
        sys.exit(1)
