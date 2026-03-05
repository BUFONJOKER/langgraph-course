import uuid

def generate_thread_id():
    '''
    This function generates a unique thread ID using UUID4.
    '''

    thread_id = str(uuid.uuid4())

    return thread_id