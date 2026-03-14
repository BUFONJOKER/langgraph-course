import uuid

def generate_thread_id():
    '''Generates a unique thread ID using UUID4. This can be used to track conversations or sessions in the chatbot.'''
    return str(uuid.uuid4())