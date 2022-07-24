from constants import (
  JSON_COMMA,
  JSON_LEFTBRACE,
  JSON_LEFTBRACKET,
  JSON_RIGHTBRACE,
  JSON_RIGHTBRACKET,
  JSON_COLON
)

'''
HOW IT WORK:
- while it is not the JSON_RIGHTBRACKET find a number follow by JSON_COMMA
- if it is JSON_RIGHTBRACKET, return the array.
'''
def parse_array(tokens: list):
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

'''
HOW IT WORK:
- first check for the key, key are string.
- then call parse on the value.
- after parse check for `,` or `}`
'''
def parse_object(tokens: list):
  json_obj = {}
  while True:
    # check for key.
    key, tokens = parse(tokens)
    if type(key) != str:
      raise SyntaxError(f'key expect to be a string but got: `{key}`')

    if key in json_obj:
      raise SyntaxError(f'object have duplicate key: {key}')

    try:
      token = tokens[0]
    except IndexError:
      raise SyntaxError('Expected `}` at the end of the object')

    # check for `:` or JSON_COLON.
    if token != JSON_COLON:
      raise SyntaxError('expect `:` character in the object')
    # now skip the `,`
    tokens = tokens[1:]

    # parse the value.
    value, tokens = parse(tokens)
    json_obj[key] = value

    try:
      token = tokens[0]
    except IndexError:
      raise SyntaxError('Expected `}` at the end of the object')

    # check for `,` or '}'.
    if token == JSON_COMMA:
      tokens = tokens[1:]
    elif token == JSON_RIGHTBRACE:
      return json_obj, tokens[1:]
    else:
      raise SyntaxError('Expected `,` at the end of the object')

def parse(tokens: list):
  token = tokens[0]

  if token == JSON_LEFTBRACKET:
    return parse_array(tokens[1:])
  elif token == JSON_LEFTBRACE:
    return parse_object(tokens[1:])
  else:
    return token, tokens[1:]
