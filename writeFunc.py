import json
import os

# list of function descriptions
functions = [
    {
        "function": "search_bing",
        "description": "Search the web for content on Bing. This allows users to search online/the internet/the web for content.",
        "arguments": [
            {
                "name": "query",
                "type": "string",
                "description": "The search query string"
            }
        ],
        "samplePrompts": ["Placeholder prompt 1", "Placeholder prompt 2"],
        "sampleResponses": ["Placeholder response 1", "Placeholder response 2"]
    },
    {
        "function": "get_current_weather",
        "description": "Get the current weather in a given location",
        "arguments": [
            {
                "name": "location",
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA"
            },
            {
                "name": "unit",
                "type": "string",
                "description": "Measurement unit for the weather. Options: 'celsius', 'fahrenheit'"
            }
        ],
        "samplePrompts": ["Placeholder prompt 1", "Placeholder prompt 2"],
        "sampleResponses": ["Placeholder response 1", "Placeholder response 2"]
    },
    {
        "function": "search_arxiv",
        "description": "Search for research papers on ArXiv. Make use of AND, OR and NOT operators as appropriate to join terms within the query.",
        "arguments": [
            {
                "name": "query",
                "type": "string",
                "description": "The search query string"
            }
        ],
        "samplePrompts": ["Placeholder prompt 1", "Placeholder prompt 2"],
        "sampleResponses": ["Placeholder response 1", "Placeholder response 2"]
    }
]

# Create a new directory called "functions" if it doesn't exist
if not os.path.exists('functions'):
    os.makedirs('functions')

# write the description of each function to a separate JSON file
for function in functions:
    filename = f'functions/{function["function"]}.json'
    with open(filename, 'w') as f:
        json.dump({"description": function}, f, indent=4)
