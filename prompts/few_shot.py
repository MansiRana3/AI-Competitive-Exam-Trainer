
def build_few_shot_prompt(examples: list, question: str) -> str:
    """
    Takes a list of example pairs and a question,
    builds a few-shot prompt string.

    WHY THIS FUNCTION:
    Instead of manually writing examples every time,
    just pass in a list of (input, output) pairs and
    your question — get a ready prompt back.

    Args:
        examples: list of dicts with 'input' and 'output' keys
        question: the actual question to ask

    Example:
        examples = [
            {"input": "A body found in the library",
             "output": "I observe the dust..."},
        ]
    """

    prompt = "Here are some examples of how to respond:\n\n"

    for i, example in enumerate(examples, 1):
        prompt += f"Example {i}:\n"
        prompt += f"Input: {example['input']}\n"
        prompt += f"Output: {example['output']}\n\n"
ompt += f"Input: {question}\n"
    prompt += f"Output:"

    return prompt
