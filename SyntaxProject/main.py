import tkinter as tk
from lexical_analyzer import LexicalAnalyzer
from syntax_analyzer import SyntaxAnalyzer

class HighlighterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Syntax Highlighter")

        self.text = tk.Text(root, wrap="word", font=("Courier New", 12))
        self.text.pack(expand=True, fill="both")
        self.text.bind("<KeyRelease>", self.on_key_release)

        self.lexer = LexicalAnalyzer()

        # Renk ayarları
        self.text.tag_config("KEYWORD", foreground="blue")
        self.text.tag_config("ID", foreground="black")
        self.text.tag_config("NUMBER", foreground="green")
        self.text.tag_config("OP", foreground="orange")
        self.text.tag_config("SEPARATOR", foreground="purple")
        self.text.tag_config("ERROR", background="red", foreground="white")

    def on_key_release(self, event=None):
        code = self.text.get("1.0", "end-1c")
        self.highlight(code)

    def highlight(self, code):
        self.text.tag_remove("KEYWORD", "1.0", "end")
        self.text.tag_remove("ID", "1.0", "end")
        self.text.tag_remove("NUMBER", "1.0", "end")
        self.text.tag_remove("OP", "1.0", "end")
        self.text.tag_remove("SEPARATOR", "1.0", "end")
        self.text.tag_remove("ERROR", "1.0", "end")

        tokens = self.lexer.analyze(code)
        for token in tokens:
            line = code[:token.start_index].count('\n') + 1
            column = token.start_index - code.rfind('\n', 0, token.start_index) - 1
            start = f"{line}.{column}"
            end = f"{line}.{column + len(token.value)}"

            tag = token.type if token.type in ["KEYWORD", "ID", "NUMBER", "OP", "SEPARATOR"] else "ERROR"
            self.text.tag_add(tag, start, end)
                # Syntax kontrolü:
        parser = SyntaxAnalyzer(tokens)
        parser.parse()

        if parser.index < len(tokens):  # Tüm token'lar işlenmediyse hata var
            self.text.tag_add("ERROR", "1.0", "end")


        # Syntax kontrolü:
        parser = SyntaxAnalyzer(tokens)
        parser.parse()

# Uygulamayı başlat
if __name__ == "__main__":
    root = tk.Tk()
    app = HighlighterApp(root)
    root.mainloop()
