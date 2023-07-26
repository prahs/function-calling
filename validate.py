import json
import argparse
import os

def validate_structure(data, schema):
    if isinstance(schema, dict):
        for key, value in schema.items():
            if key not in data:
                print(f"Error: Missing key '{key}' in function file.")
            elif isinstance(value, dict) or isinstance(value, list):
                validate_structure(data[key], value)
            elif not isinstance(data[key], value):
                print(f"Error: Key '{key}' should be of type '{value.__name__}', but found type '{type(data[key]).__name__}'.")
    elif isinstance(schema, list):
        if len(schema) == 0:
            return
        for item in data:
            validate_structure(item, schema[0])

def validate_file(function_file):
    # Define the structure of the expected JSON file
    schema = {
        "functionMetaData": {
            "function": str,
            "description": str,
            "arguments": [{"name": str, "type": str, "description": str}]
        },
        "samplePromptResponsePairs": [{"prompt": str, "response": dict}]
    }

    # Check if the file exists
    if not os.path.exists(f'functions/{function_file}'):
        print(f"Error: File '{function_file}' does not exist in the 'functions' directory.")
        return

    try:
        # Read the function JSON
        with open(f'functions/{function_file}', 'r') as f:
            function = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: File '{function_file}' is not a valid JSON file or it is empty.")
        return

    # Validate the structure of the JSON file
    validate_structure(function, schema)

    print(f"Validation complete for {function_file}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Validate a function JSON file.')
    parser.add_argument('function_file', type=str, help='The name of the function file to validate.')
    args = parser.parse_args()

    validate_file(args.function_file)
