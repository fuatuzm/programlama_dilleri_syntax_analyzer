from lexical_analyzer import LexicalAnalyzer
from syntax_analyzer import SyntaxAnalyzer

code = "if (x > 3) { x = x + 1; }"
lexer = LexicalAnalyzer()
tokens = lexer.analyze(code)

parser = SyntaxAnalyzer(tokens)
parser.parse()
