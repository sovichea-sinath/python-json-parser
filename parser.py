from constants import (
  JSON_COMMA,
  JSON_LEFTBRACE,
  JSON_LEFTBRACKET,
  JSON_RIGHTBRACKET,
)

'''
HOW IT WORK:
- while it is not the JSON_RIGHTBRACKET find a number follow by JSON_COMMA
- if it is JSON_RIGHTBRACKET, return the array.
'''
def parse_array(tokens: list[str]):
  json_array = []
  # python list does not have a .get() method. this is a work around to check for `]`.
  try:
    token = tokens[0]
  except IndexError:
    raise SyntaxError('Expected `]` at the end of the array')

  if token == JSON_RIGHTBRACKET:
    return json_array, tokens[1:]

  while True:
    json, tokens = parse(tokens)
    json_array.append(json)

    # python list does not have a .get() method. this is a work around to check for `]`.
    try:
      token = tokens[0]
    except IndexError:
      raise SyntaxError('Expected `]` at the end of the array')

    # check for comma and bracket after each array value.
    if token == JSON_COMMA:
      tokens = tokens[1:]
      continue
    elif token == JSON_RIGHTBRACKET:
      return json_array, tokens[1:]

    raise SyntaxError('Expected `,` in the array')

def parse_object(tokens: list[str]):
  return {}, tokens

def parse(tokens: list[str]):
  token = tokens[0]

  if token == JSON_LEFTBRACKET:
    return parse_array(tokens[1:])
  elif token == JSON_LEFTBRACE:
    return parse_object(tokens[1:])
  else:
    return token, tokens[1:]
