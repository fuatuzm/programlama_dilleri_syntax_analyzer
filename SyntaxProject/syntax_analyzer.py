class SyntaxAnalyzer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def current(self):
        if self.index < len(self.tokens):
            return self.tokens[self.index]
        return None

    def match(self, expected_type, expected_value=None):
        token = self.current()
        if token and token.type == expected_type and (expected_value is None or token.value == expected_value):
            self.index += 1
            return True
        return False

    def parse(self):
        if not self.statement():
            print("Syntax Error")
        elif self.index < len(self.tokens):
            print("Syntax Error: Unexpected token at end.")
        else:
            print("Syntax OK")

    def statement(self):
        token = self.current()
        if token and token.value == "if":
            return self.if_statement()
        elif token and token.type == "ID":
            return self.assignment()
        return False

    def if_statement(self):
      
        if not self.match("KEYWORD", "if"):
            return False
        if not self.match("SEPARATOR", "("):
            return False
        if not self.expr():
            return False
        if not self.match("SEPARATOR", ")"):
            return False
        if not self.block():  # Artık burada birden fazla işlem destekleniyor
            return False
        return True

    
    def block(self):
         if not self.match("SEPARATOR", "{"):
            return False
         while not self.match("SEPARATOR", "}"):
            if not self.statement():
             return False
         return True


    def assignment(self):
        if not self.match("ID"):
            return False
        if not self.match("OP", "="):
            return False
        if not self.expr():
            return False
        if not self.match("SEPARATOR", ";"):
            return False
        return True

    def expr(self):
        if not self.term():
            return False
        while True:
            token = self.current()
            if token and token.type == "OP" and token.value in ("+", "-", "*", "/", ">", "<", "==", "!=", "<=", ">="):
                self.index += 1
                if not self.term():
                    return False
            else:
                break
        return True

    def term(self):
        token = self.current()
        if token is None:
            return False
        if token.type in ("ID", "NUMBER"):
            self.index += 1
            return True
        return False
