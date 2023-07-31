---
task_categories:
- question-answering
- conversational
- text-generation
language:
- en
tags:
- function call
- function calling
- function-calling
size_categories:
- n<1K
---
# Trelis Function Calling Datasets

We offer two datasets for training language models to support function calling:

1. [Function Calling Dataset](https://huggingface.co/datasets/Trelis/function_calling)
2. [Function Calling Extended Dataset](https://huggingface.co/datasets/Trelis/function_calling_extended)

The extended dataset has 33 prompt-response pairs, compared to 11 for the open-source dataset.

Both datasets were human generated (i.e. did not make use of Llama or OpenAI's GPT models etc.). This is important because Meta and OpenAI terms do not allow their language models to be used to train other models.

## Licensing

### Function Calling Dataset

The Function Calling dataset is licensed under Apache 2.

You can submit new functions by creating a new branch and requesting to merge a pull request. All contributions must allow for the Apache 2 license to be used (you cannot use ChatGPT or Llama or any other restricted model to generate the prompts). Make sure to run validate.py on your function.json to ensure it is properly structured.

### Function Calling Extended Dataset

The Function Calling Extended dataset is commercially licensed. Users can purchase a license for €9.99 per device from [here](https://buy.stripe.com/00g4h2cWh5TJ9IQ28c). Users will receive access within 24 hours of their purchase. 

Examples of license requirements:
- Training on a CPU = 1 license required.
- Training on a CPU + 1 GPU/TPU = 1 license required. (CPU is considered ancillary in this case)
- Training a model on 2 GPUs = 2 licenses required.

Licenses are transferable across different machines provided they are not running simultaneously. The license is solely for training language models. For other use cases, please reach out to us.

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

## Testing JSON Structure

A script named `validate.py` can be used to validate the structure of a function JSON file. It checks for the presence and correct types of all necessary keys in the JSON structure.

To use the script, call it from the command line with the name of the function file as an argument:

```
python validate.py my_function.json

```

