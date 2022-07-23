import unittest
from lexer import lex


class TestStringMethods(unittest.TestCase):
  def test_parser(self):
    tokens = lex('{"foo": [1, 2, {"bar": 2}]}')
    unittest.TestCase.assertEquals(self, tokens, ['{', 'foo', ':', '[', 1, ',', 2, ',', '{', 'bar', ':', 2, '}', ']', '}'])


if __name__ == "__main__":
  unittest.main()
