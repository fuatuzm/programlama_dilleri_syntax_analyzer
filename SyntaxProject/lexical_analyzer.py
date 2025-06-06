class Token:
    def __init__(self, type, value, start_index, end_index):
        self.type = type
        self.value = value
        self.start_index = start_index
        self.end_index = end_index

    def __repr__(self):
        return f"{self.type}({self.value}) [{self.start_index}-{self.end_index}]"

class LexicalAnalyzer:
    def __init__(self):
        self.keywords = {"if", "else", "while", "for", "int", "float", "return", "void"}
        self.operators = {'+', '-', '*', '/', '=', '<', '>', '!', '==', '!=', '<=', '>='}
        self.separators = {'(', ')', '{', '}', ';', ',', '[', ']'}

    def analyze(self, code):
        tokens = []
        i = 0
        while i < len(code):
            c = code[i]

            if c.isspace():
                i += 1
                continue

            start = i

            # Keywords or Identifiers
            if c.isalpha() or c == "_":
                while i < len(code) and (code[i].isalnum() or code[i] == "_"):
                    i += 1
                value = code[start:i]
                token_type = "KEYWORD" if value in self.keywords else "ID"
                tokens.append(Token(token_type, value, start, i))

            # Numbers
            elif c.isdigit():
                while i < len(code) and code[i].isdigit():
                    i += 1
                tokens.append(Token("NUMBER", code[start:i], start, i))

            # Operators (2 karakterli ve 1 karakterli)
            elif c in "=!<>":
                if i+1 < len(code) and code[i+1] == '=':
                    tokens.append(Token("OP", code[i:i+2], start, i+2))
                    i += 2
                else:
                    tokens.append(Token("OP", c, start, i+1))
                    i += 1
            elif c in self.operators:
                tokens.append(Token("OP", c, start, i+1))
                i += 1

            # Separators
            elif c in self.separators:
                tokens.append(Token("SEPARATOR", c, start, i+1))
                i += 1

            # Unknown / Error
            else:
                tokens.append(Token("MISMATCH", c, start, i+1))
                i += 1

        return tokens
