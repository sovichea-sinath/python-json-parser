from constants import *
'''
WHAT IT WILL DO:
  - check the the first char if it is a quote.
  if not return None and the original string.
  - if found the quote, push every other char to a string untill found the
  ending quote.
  - if the ending quote is not found and EOF hit, return error?
'''
def lex_string(string: str):
  json_string = ''

  if string[0] != JSON_QUOTE:
    return None, string

  string = string[1:]

  for c in string:
    if c == JSON_QUOTE:
      return json_string, string[len(json_string)+1:]
    json_string += c
  
  raise EOFError(f'Missing ending { JSON_QUOTE } character')


'''
WHAT IT WILL DO:
  - check the string until we cannot constuct a number no more.
'''
def lex_number(string: str):
  if string[0] not in JSON_DECIMAL_NUMBER:
    return None, string

  json_number = ''
  is_decimal_point_exist = False

  for c in string:
    if c in JSON_DECIMAL_NUMBER:
      json_number += c
      continue
    
    if c == JSON_DECIMAL_POINT and not is_decimal_point_exist:
      json_number += c
      is_decimal_point_exist = True
      continue
    elif c == JSON_DECIMAL_POINT and is_decimal_point_exist:
      raise SyntaxError('Decimal point "." already exist')

    break

  rest = string[len(json_number):]
  return (float(json_number), rest) if is_decimal_point_exist == True else (int(json_number), rest)

'''
HOW IT WORK: just match the string.
'''
def lex_bool(string: str):
  true_len = len(JSON_TRUE)
  false_len = len(JSON_FALSE)

  if len(string) >=true_len and string[:true_len] == JSON_TRUE:
    return True, string[true_len:]
  elif len(string) >=false_len and string[:false_len] == JSON_FALSE:
    return False, string[false_len:]

  return None, string

'''
HOW IT WORK: just match the string.
'''
def lex_null(string: str):
  null_len = len(JSON_NULL)
  if len(string) >= null_len and string[:null_len] == JSON_NULL:
    return True, string[null_len]

  return None, string

def lex(string: str):
  tokens: list[str] = []

  # loop until the string is ''. whe pop left 1 char per iteration.
  while len(string):
    json_string, string = lex_string(string)
    if json_string is not None:
      tokens.append(json_string)
      continue

    json_bool, string = lex_bool(string)
    if json_bool is not None:
      tokens.append(json_bool)
      continue

    json_number, string = lex_number(string)
    if json_number is not None:
      tokens.append(json_number)
      continue

    json_null, string = lex_null(string)
    if json_null is not None:
      tokens.append(json_null)
      continue

    # skip any kind of white space.
    if string[0] in JSON_WHITESPACE:
      string = string[1:]
    elif string[0] in JSON_SYNTAX:
      tokens.append(string[0])
      string = string[1:]
    else:
      raise SyntaxError(f'Unexpected character: {string[0]}')
  
  return tokens

if __name__ == '__main__':
  pass
