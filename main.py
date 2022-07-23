from lexer import lex

def main():
  assert lex('{"foo": [1, 2, {"bar": 2}]}') == ['{', 'foo', ':', '[', 1, ',', 2, ',', '{', 'bar', ':', 2, '}', ']', '}']

if __name__ == "__main__":
  main()
