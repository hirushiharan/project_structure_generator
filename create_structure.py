import json
import os
import argparse

def create_structure(path, structure):
    """
    Recursively create directories and files based on a structure dictionary.
    
    Args:
        path (str): Current directory path where items will be created.
        structure (dict): Dictionary defining the structure (folders as dicts, files as strings).
    """
    for name, content in structure.items():
        full_path = os.path.join(path, name)
        if isinstance(content, dict):
            # If content is a dictionary, create a directory and recurse
            os.makedirs(full_path, exist_ok=True)
            create_structure(full_path, content)
        elif isinstance(content, str):
            # If content is a string, create a file with that content
            with open(full_path, 'w') as f:
                f.write(content)
        else:
            # Warn about unexpected types and skip them
            print(f"Warning: Invalid type for {name}: {type(content)}. Skipping.")

if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Create project structure from JSON.")
    parser.add_argument("json_file", help="Path to the JSON file describing the structure.")
    parser.add_argument(
        "output_dir",
        nargs='?',
        default=".",
        help="Output directory (default: current directory)."
    )
    args = parser.parse_args()

    # Load the JSON file
    try:
        with open(args.json_file, 'r') as f:
            json_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: The file {args.json_file} was not found.")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: The file {args.json_file} contains invalid JSON.")
        exit(1)

    # Validate that the JSON has exactly one top-level key
    if not isinstance(json_data, dict) or len(json_data) != 1:
        print("Error: JSON should be a dictionary with exactly one top-level key.")
        exit(1)

    # Create the structure starting at the output directory
    create_structure(args.output_dir, json_data)