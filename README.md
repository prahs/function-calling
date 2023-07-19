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
WORK IN PROGRESS

## Prompt Template

```# prompt_template = "### System: {systemPrompt}\n### User: {userPrompt}\n### Assistant: {assistantResponse}"```

## systemPrompt Training Set

Three defined functions:
1. search_bing, 87 tokens
 ```{
    "name": "search_bing",
    "description": "Search the web for content on Bing. This allows users to search online/the internet/the web for content.",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "The search query string",
            }
        },
        "required": ["query"],
    },
}```

2. get_current_weather, 110 tokens
```{
    "name": "get_current_weather",
    "description": "Get the current weather in a given location",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA",
            },
            "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
        },
        "required": ["location"],
    },
}```

3. search_arxiv, 93 tokens
```{
    "name": "search_arxiv",
    "description": "Search for research papers on ArXiv. Make use of AND, OR and NOT operators as appropriate to join terms within the query.",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "The search query string",
            }
        },
        "required": ["query"],
    },
}```

Instructions on use of functions (instructions):
"To make a function call, respond immediately with a json object containing the function_call role, the name of the function, and the function arguments:

{
    "role": "function_call",
    "name": "function_name",
    "arguments": {
        "argument_name_1": "argument_value_1",
        "argument_name_2": "argument_value_2"
    }
}
"

## userPrompt and assistantResponse Training Set
### A. Three function-requiring prompts for each function, each followed by a function invocation. One non-function requiring prompts. (3 x 2 x 3 = 18 prompts).

1. search_bing

i.

userPrompt = Search the internet for Irish stew recipes.

assistantResponse = {
    "role": "function_call",
    "name": "search_bing",
    "arguments": {
        "query": "irish stew recipes"
    }
}

ii.

userPrompt = Search bing for instructions to fly a kite.

assistantResponse = {
    "role": "function_call",
    "name": "search_bing",
    "arguments": {
        "query": "instructions to fly a kite"
    }
}

iii.

userPrompt = Find restaurant recommendations for Dublin on the web.

assistantResponse = {
    "role": "function_call",
    "name": "search_bing",
    "arguments": {
        "query": "Dublin restaurant recommendations"
    }
}

2. get_current_weather

i.

userPrompt = What's the weather in Lagos now? My friend is over there right now.

assistantResponse = {
    "role": "function_call",
    "name": "get_current_weather",
    "arguments": {
        "location": "lagos, Nigeria"
        "unit": "celsius"
    }
}

ii.

userPrompt = How hot is it in Berlin? I'm wondering if I'll go out for a cycle.

assistantResponse = {
    "role": "function_call",
    "name": "get_current_weather",
    "arguments": {
        "location": "Berlin, Germany"
        "unit": "celsius"
    }
}

iii.

userPrompt = I'm going on holidays later today. How's the weather in Boston?

assistantResponse = {
    "role": "function_call",
    "name": "get_current_weather",
    "arguments": {
        "location": "Boston, Massachusetts"
        "unit": "fahrenheit"
    }
}

3. search_arxiv

userPrompt = ...

assistantResponse = ...

### B. Nine prompts not requiring the use of defined functions. Each followed by non-function responses. (9 prompts).

i.

userPrompt = Search google for paintings by Michelangelo

assistantResponse = There are no functions allowing me to search google, but I can search the internet using Bing if you ask.

ii.

userPrompt = What is the name of the largest breed of dog?

assistantResponse = The Great Dane is typically seen to be the largest dog breed, in terms of height. Although they aren't heaviest breed, they can be up to 30 inches tall in height.

iii.

userPrompt = What is the weather forecast for two weeks from now?

assistantResponse = There is not function to get the weather forecast two weeks from now, but I can help you with the weather today if you provide a location.

iv.

...

## systemPrompt and user/assistantResponse Training Set Combinations

Each function has three function-requiring prompts and six non-function-requiring prompts.

For function1, we can define training rows consisting of:
- systemPrompt | userPrompt | assistantPrompt
- instructions + function1 | function-requiring prompt | function invocation (x3)
- instructions + function1 | non-function-requiring prompt | non-function response (x9)
- instructions + function1 + function2 | function-requiring prompt | function invocation (x3)
- instructions + function1 + function2 | non-function-requiring prompt | non-function response (x9)
- instructions + function1 + function2 + function3 | function-requiring prompt | function invocation (x3)
- instructions + function1 + function2 + function3 | non-function-requiring prompt | non-function response (x9)

= 36 rows.

Then repeat this for function2 (x36) and function3 (x36).
Then shuffle the rows.
Then extract the last 20 rows as a test set.

train-function-calling rows = 36x3 - 20 = 88
test-function-calling rows = 20