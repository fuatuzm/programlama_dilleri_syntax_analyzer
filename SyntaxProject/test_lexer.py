from lexical_analyzer import LexicalAnalyzer

code = "int x = 5;\nif (x > 3) { x = x + 1; }"

lexer = LexicalAnalyzer()
tokens = lexer.analyze(code)

for token in tokens:
    print(token)
