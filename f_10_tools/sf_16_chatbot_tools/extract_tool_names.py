def extract_tool_names(message) -> list[str]:
  '''
  Extract tool names from streamed LLM messages.
  '''

  tool_names = []

  for tool_call_chunk in getattr(message, 'tool_call_chunks', []) or []:
    name = tool_call_chunk.get('name') if isinstance(tool_call_chunk, dict) else getattr(tool_call_chunk, 'name', None)
    if name:
      tool_names.append(name)

  for tool_call in getattr(message, 'tool_calls', []) or []:
    name = tool_call.get('name') if isinstance(tool_call, dict) else getattr(tool_call, 'name', None)
    if name:
      tool_names.append(name)

  return list(dict.fromkeys(tool_names))
