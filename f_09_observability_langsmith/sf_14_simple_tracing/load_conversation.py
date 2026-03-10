def load_conversation(thread_id, workflow):
  '''
  Load conversation history for a given thread_id using the workflow's state management.
  '''

  CONFIG = {'configurable':{'thread_id': thread_id}}
  state = workflow.get_state(config=CONFIG)
  result = state.values.get('messages', [])
  return result