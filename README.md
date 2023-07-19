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
Three example types are used:
1. Prompts where a function should be called.
2. Prompts where there is a similar function.
3. Prompts where there is no function available.