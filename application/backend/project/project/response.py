class Response():
    '''
    result = {\n
        'status': 'success',\n
        ...
    }\n
    messages = {\n
        'success': 'This operation was completed successfully.',\n
        'error': 'Error occurred during this operation.',\n
        'unique': 'This field must be unique.',\n
        'required': 'This field is required.',\n
        'exists': 'This object already exists.',\n
        'does_not_exist': 'This object does not exist.',\n
        'no_objects': 'No objects available to conduct this operation.',\n
        'unauthenticated': 'This operation requires an authenticated user.',\n
        'unauthorised': 'This operation is not authorised.',\n
        'other': 'Unknown error.'\n
    }\n
    '''
    
    messages = {
        'success': 'This operation was completed successfully.',
        'error': 'Error occurred during this operation.',
        'unique': 'This field must be unique.',
        'required': 'This field is required.',
        'exists': 'This object already exists.',
        'does_not_exist': 'This object does not exist.',
        'no_objects': 'No objects available to conduct this operation.',
        'unauthenticated': 'This operation requires an authenticated user.',
        'unauthorised': 'This operation is not authorised.',
        'other': 'Unknown error.'
    }

    def __init__(self):
        self.result = {
            'status': 'success',
        }

    def set_message(self, field, message='', code='', as_list=True):
        if code:
            message = self.messages.get(code)
        if not as_list:
            self.result[field] = message
            return
        try:
            self.result[field].append(message)
        except:
            self.result[field] = [message]
            
    def set_messages(self, field, messages):
        try:
            self.result[field].extend(messages)
        except:
            self.result[field] = messages

    def set_error(self, field, error='', code='', as_list=True):
        self.result['status'] = 'error'
        if code:
            error = self.messages.get(code)
        if not as_list:
            self.result[field] = error
            return
        try:
            self.result[field].append(error)
        except:
            self.result[field] = [error]
            
    def set_errors(self, field, errors, replace=False):
        self.result['status'] = 'error'
        try:
            if not replace:
                self.result[field].extend(errors)
                return
            raise Exception
        except:
            self.result[field] = errors
    
    def set_choice_error(self, field, choices):
        self.result['status'] = 'error'
        message = 'available choices are '
        for choice in choices:
            message += f'"{choice}", '
        message = message[:-2]
        try:
            self.result[field].append(message)
        except:
            self.result[field] = [message]
        