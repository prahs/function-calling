---
task_categories:
- question-answering
language:
- en
tags:
- code
size_categories:
- n<1K
license: apache-2.0
---
# README

This repository contains a Python script to generate a training and testing dataset for OpenAI's ChatGPT from a collection of functions and their sample prompts and responses.

## File Structure

- `functions/`: This directory contains function files, each of which is a JSON file with a specific structure that describes a function and its sample prompts and responses.
- `generate_dataset.py`: This Python script generates the training and testing dataset CSV files.

## JSON File Structure

Each function file should be a JSON file with the following structure:

```json
{
    "functionMetaData": {
        "function": "function_name",
        "description": "function_description",
        "arguments": [
            {
                "name": "argument_name",
                "type": "argument_type",
                "description": "argument_description"
            },
            ...
        ]
    },
    "samplePromptResponsePairs": [
        {
            "prompt": "sample_prompt",
            "response": {
                "arguments": {
                    "argument_name": "argument_value",
                    ...
                }
            }
        },
        ...
    ]
}
```

The `functionMetaData` object describes the function. The `samplePromptResponsePairs` array contains sample prompts and responses for the function.

## Dataset Generation

To generate the dataset, run the `generate_dataset.py` script. This script will iterate over each function file and generate a CSV row for each sample prompt-response pair.

## CSV File Structure

The generated CSV file has the following columns:

- `systemPrompt`: The system's prompt, which includes the descriptions of two functions (the current function and a randomly selected other function) and instructions on how to call a function.
- `userPrompt`: The user's prompt.
- `assistantResponse`: The assistant's response.

## Formatting the Training and Test Sets

For training the assistant model, a specific prompt format is required. The Python script `prepare_dataset.py` is provided to format the training and test sets.

This script embeds each part of the dialogue (system prompt, user prompt, and assistant response) within specific markers that indicate their role in the conversation. For example, the system prompt is embedded within `<<SYS>>` and `<</SYS>>` markers, while the user prompt is embedded within `[INST]` and `[/INST]` markers.

The `prepare_dataset` function within this script applies this formatting to each dialogue in the training or test set, creating a new set with the formatted dialogues.

The function is called as follows:

```python
def prepare_dataset(dataset, tokenizer):
    # Define the roles and markers
    B_SYS, E_SYS = "<<SYS>>", "<</SYS>>"
    B_INST, E_INST = "[INST]", "[/INST]"

    # Create the formatted text with the correct roles for each part of the dialogue
    formatted_dataset = dataset.map(
        lambda x: {
            "input_text": "".join([
                f"{B_INST} {B_SYS}{x['systemPrompt'].strip()}{E_SYS} \n",
                f"{x['userPrompt'].strip()} {E_INST} \n",
                f"{x['assistantResponse'].strip()}",  # appending the EOS token in TextData...
            ]),
            "response_text": "".join([
                f"{x['assistantResponse'].strip()}",  # appending the EOS token in TextData...
            ]),
        }
    )
```

## Testing JSON Structure

A script named `validate.py` can be used to validate the structure of a function JSON file. It checks for the presence and correct types of all necessary keys in the JSON structure.

To use the script, call it from the command line with the name of the function file as an argument:

```
python validate.py my_function.json

```

