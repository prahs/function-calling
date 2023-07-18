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

```# prompt_template = "### System: {systemPrompt}\n### User {userPrompt}\n### Assistant: {assistantResponse}"```

## systemPrompt Training Set

Three defined functions:
1. 
1. 
1. 

Instructions on use of functions (instructions):
""

## userPrompt and assistantResponse Training Set
1. Three function-requiring prompts for each function, each followed by a function invocation, i.e. |<call-function>| (3 x 3 = 9 prompts).
1. Nine prompts not requiring the use of defined functions. Each followed by non-function responses. (9 prompts).

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