# gpt-to-chatgpt-py
Convert a regular GPT call into a ChatGPT call

TYPESCRIPT VERSION HERE -> https://github.com/bramses/gpt-to-chatgpt-ts

## Functions

### toChatML()

Converts a string message into a Chat Markup Language (ChatML) object.

#### Usage
```python
toChatML(message:str, options:Optional[dict]=None) -> List[dict]
```

#### Arguments

- message: The string message to be converted to ChatML.
- options (optional): A dictionary that can contain the following keys:
  - system_messages: A list of strings that represent system messages to be added to the ChatML object.
  - role: The role of the message (either Role.USER or Role.ASSISTANT).

#### Examples

```python
toChatML('hello')
# Output: [{'role': Role.USER, 'content': 'hello'}]
```

```python
toChatML('hello', {'system_messages': ['hi'], 'role': Role.ASSISTANT})
# Output: [{'role': Role.SYSTEM, 'content': 'hi'}, {'role': Role.ASSISTANT, 'content': 'hello'}]
```

### get_message()

Extracts the message content from a response object.

#### Usage

```python
get_message(response: dict, options: Optional[dict] = None) -> Union[str, dict]
```

#### Arguments

- response: The response object from which to extract the message content.
- options (optional): A dictionary that can contain the following keys:
  - usage: A boolean value that indicates whether to return the usage information of the response.
  - role: A boolean value that indicates whether to return the role of the message.
  - isMessages: A boolean value that indicates whether to return the message as a list of messages.

#### Examples

```python
get_message(test_response)
# Output: 'The 2020 World Series was played in Arlington, Texas at the Globe Life Field, which was the new home stadium for the Texas Rangers.'

get_message(test_response, {'usage': True, 'role': True, 'isMessages': True})
# Output: {'usage': {'prompt_tokens': 56, 'completion_tokens': 31, 'total_tokens': 87},
#          'roles': ['assistant'],
#          'messages': ['The 2020 World Series was played in Arlington, Texas at the Globe Life Field, which was the new home stadium for the Texas Rangers.']}

get_message(test_response, {'usage': True, 'role': True})
# Output: {'usage': {'prompt_tokens': 56, 'completion_tokens': 31, 'total_tokens': 87},
#          'role': 'assistant',
#          'message': 'The 2020 World Series was played in Arlington, Texas at the Globe Life Field, which was the new home stadium for the Texas Rangers.'}

get_message(test_response, {'usage': True, 'isMessages': True})
# Output: {'usage': {'prompt_tokens': 56, 'completion_tokens': 31, 'total_tokens': 87},
#          'messages': ['The 2020 World Series was played in Arlington, Texas at the Globe Life Field, which was the new home stadium for the Texas Rangers.']}
```
