from enum import Enum

class Role(Enum):
    SYSTEM = 0
    USER = 1
    ASSISTANT = 2

def role_to_string(role):
    if role == Role.SYSTEM:
        return 'system'
    elif role == Role.USER:
        return 'user'
    elif role == Role.ASSISTANT:
        return 'assistant'
    else:
        return 'unknown'

def toChatML(original, options = {'system_messages': None, 'role': Role.USER }):
    messages = []

    if 'system_messages' in options and options['system_messages'] is not None:
        # lambda for message in system_messages to create a dict with role SYSTEM
        messages.extend([{'role' : role_to_string(Role.SYSTEM), 'content': message} for message in options['system_messages']])

    if 'role' not in options:
        options['role'] = Role.USER

    messages.append({'role' : role_to_string(options['role']), 'content': original})
    
    return messages


def get_message(response, options = { 'usage': False, 'role': False, 'isMessages': False }):
    
    response_dict = {}

    if 'usage' in options and options['usage'] == True:
        response_dict['usage'] = response['usage']


    if 'isMessages' in options and options['isMessages'] == True:
        response_dict['messages'] = []    

        for message in response['choices']:
            response_dict['messages'].append(message['message']['content'])

        if 'role' in options and options['role'] == True:
                response_dict['roles'] = []
                for message in response['choices']:
                    response_dict['roles'].append(message['message']['role'])

    # if response_dict is not Empty
    if response_dict != {}:
        if ('isMessages' not in options) or ('isMessages' in options and options['isMessages'] == False):
            response_dict['message'] = response['choices'][0]['message']['content']
            if 'role' in options and options['role'] == True:
                response_dict['role'] = response['choices'][0]['message']['role']
        return response_dict

    # base case just return the message    
    return response['choices'][0]['message']['content']