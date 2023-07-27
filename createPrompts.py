import json
import os
import random
import csv
import math

# Get the list of function files
function_files = os.listdir('functions')

# Open the CSV file for writing
with open('prompts.csv', 'w', newline='') as csvfile:
    # Create a CSV writer
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(['systemPrompt', 'userPrompt', 'assistantResponse'])

    # Create a list to store the rows
    rows = []

    # Iterate over each function file
    for function_file in function_files:
        # Read the function JSON
        with open(f'functions/{function_file}', 'r') as f:
            function = json.load(f)

        # Randomly select another function file
        other_function_file = random.choice(function_files)
        while other_function_file == function_file:
            other_function_file = random.choice(function_files)

        # Read the other function JSON
        with open(f'functions/{other_function_file}', 'r') as f:
            other_function = json.load(f)

        # Iterate over each prompt-response pair
        for pair in function["samplePromptResponsePairs"]:
            # Construct the system prompt
            system_prompt = "You are a helpful research assistant. The following functions are available for you to fetch further data to answer user questions, if relevant:\n\n"

            # Randomize the order of function descriptions
            if random.choice([True, False]):
                system_prompt += json.dumps(function["functionMetaData"], indent=4, separators=(',', ': '))
                system_prompt += "\n\n"
                system_prompt += json.dumps(other_function["functionMetaData"], indent=4, separators=(',', ': '))
            else:
                system_prompt += json.dumps(other_function["functionMetaData"], indent=4, separators=(',', ': '))
                system_prompt += "\n\n"
                system_prompt += json.dumps(function["functionMetaData"], indent=4, separators=(',', ': '))

            system_prompt += """
                \n\nTo call a function, respond - immediately and only - with a JSON object of the following format:
                {
                    "function": "function_name",
                    "arguments": {
                        "argument1": "argument_value",
                        "argument2": "argument_value"
                    }
                }
                """

            # Get the user prompt
            user_prompt = pair["prompt"]

            # Get the assistant response
            assistant_response = json.dumps(pair["response"], indent=4, separators=(',', ': '))

            # Create a function call using the function name and the assistant response
            function_call = {
                "function": function["functionMetaData"]["function"],
                "arguments": json.loads(assistant_response)
            }

            # Convert the function call to a JSON string
            assistant_response = json.dumps(function_call, indent=4, separators=(',', ': '))

            # Add the row to the list
            rows.append([system_prompt, user_prompt, assistant_response])

    # Write the rows to the CSV file
    writer.writerows(rows)

    # Shuffle the rows
    random.shuffle(rows)

    # Calculate the number of test samples
    num_test_samples = math.ceil(len(rows) * 0.2)

    # Split the rows into train and test
    test_rows = rows[:num_test_samples]
    train_rows = rows[num_test_samples:]

    # Write the rows to the CSV files
    with open('test.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['systemPrompt', 'userPrompt', 'assistantResponse'])
        writer.writerows(test_rows)

    with open('train.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['systemPrompt', 'userPrompt', 'assistantResponse'])
        writer.writerows(train_rows)

