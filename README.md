# Project Structure Generator

A Python script to automate the creation of project folder structures based on a JSON input.

## Features

- Create directories and files as defined in a JSON file.
- Supports nested folder structures.
- Allows specifying file contents in the JSON.
- Command-line interface for easy usage.

## Installation

Clone this repository and navigate to the project folder:

```sh
git clone https://github.com/yourusername/Project-Structure-Generator.git
cd Project-Structure-Generator
```

Ensure you have Python 3 installed.

## Usage

Run the script with a JSON file defining the project structure:

```sh
python create_structure.py path/to/structure.json [output_directory]
```

- `structure.json` should define the folder and file structure.
- `[output_directory]` (optional) specifies where the structure should be created. Defaults to the current directory.

## Example JSON Structure

```json
{
    "email-classification-poc": {
        "data": {},
        "scripts": {
            "fetch_emails.py": "",
            "classify_emails.py": "",
            "store_emails.py": "",
            "scheduler.py": "",
            "train_model.py": ""
        },
        "config": {
            "settings.py": ""
        },
        "models": {
            "email_classifier.pkl": ""
        },
        "requirements.txt": "",
        "README.md": ""
    }
}
```

## Contributing

Feel free to submit issues or pull requests to enhance functionality.

## License

This project is licensed under the MIT License.
