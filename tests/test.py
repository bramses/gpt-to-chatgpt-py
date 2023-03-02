from src.gpt_to_chatgpt import toChatML, get_message, Role, role_to_string


def test_toChatML():
    print('Testing toChatML()')
    assert toChatML('hello') == [{'role': role_to_string(Role.USER), 'content': 'hello'}]
    print('toChatML() passed')


def test_toChatML_with_options():
    print('Testing toChatML() with options')
    assert toChatML('hello', {'system_messages': ['hi'], 'role': Role.ASSISTANT}) == [
        {'role': role_to_string(Role.SYSTEM), 'content': 'hi'}, {'role': role_to_string(Role.ASSISTANT), 'content': 'hello'}]
    
    assert toChatML('hello', {'system_messages': ['hi']}) == [
        {'role': role_to_string(Role.SYSTEM), 'content': 'hi'}, {'role': role_to_string(Role.USER), 'content': 'hello'}]
    print('toChatML() with options passed')


test_response = {
    'id': 'chatcmpl-6p9XYPYSTTRi0xEviKjjilqrWU2Ve',
    'object': 'chat.completion',
    'created': 1677649420,
    'model': 'gpt-3.5-turbo',
    'usage': {'prompt_tokens': 56, 'completion_tokens': 31, 'total_tokens': 87},
    'choices': [
        {
            'message': {
                'role': 'assistant',
                'content': 'The 2020 World Series was played in Arlington, Texas at the Globe Life Field, which was the new home stadium for the Texas Rangers.'},
            'finish_reason': 'stop',
            'index': 0
        }
    ]
}


def test_get_message():
    print('Testing get_message()')
    assert get_message(
        test_response) == 'The 2020 World Series was played in Arlington, Texas at the Globe Life Field, which was the new home stadium for the Texas Rangers.'
    print('get_message() passed')


def test_get_message_with_options():
    print('Testing get_message() with options')
    assert get_message(test_response, {'usage': True, 'role': True, 'isMessages': True}) == {
        'usage': {'prompt_tokens': 56, 'completion_tokens': 31, 'total_tokens': 87},
        'roles': ['assistant'],
        'messages': ['The 2020 World Series was played in Arlington, Texas at the Globe Life Field, which was the new home stadium for the Texas Rangers.']}
    
    assert get_message(test_response, {'usage': True, 'role': True}) == {
        'usage': {'prompt_tokens': 56, 'completion_tokens': 31, 'total_tokens': 87},
        'role': 'assistant',
        'message': 'The 2020 World Series was played in Arlington, Texas at the Globe Life Field, which was the new home stadium for the Texas Rangers.'}

    assert get_message(test_response, {'usage': True, 'role': True}) == {
        'usage': {'prompt_tokens': 56, 'completion_tokens': 31, 'total_tokens': 87},
        'role': 'assistant',
        'message': 'The 2020 World Series was played in Arlington, Texas at the Globe Life Field, which was the new home stadium for the Texas Rangers.'}

    assert get_message(test_response, {'usage': True, 'isMessages': True}) == {
        'usage': {'prompt_tokens': 56, 'completion_tokens': 31, 'total_tokens': 87},
        'messages': ['The 2020 World Series was played in Arlington, Texas at the Globe Life Field, which was the new home stadium for the Texas Rangers.']}
    print('get_message() with options passed')


if __name__ == '__main__':
    print('Running tests...')
    print('----------------')
    test_toChatML()
    test_toChatML_with_options()
    test_get_message()
    test_get_message_with_options()
