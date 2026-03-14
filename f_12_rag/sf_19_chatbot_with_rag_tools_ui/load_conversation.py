def load_conversation(thread_id, workfow):
    '''Load conversation history of given thread_id using the workflow state management'''

    CONFIG = {'configurable':{'thread_id':thread_id}}

    state = workfow.get_state(config=CONFIG)

    result = state.values.get('messages',[])

    return result