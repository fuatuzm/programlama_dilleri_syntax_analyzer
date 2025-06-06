# 📘 Real-Time Grammar-Based Syntax Highlighter with GUI

Bu proje, Bursa Teknik Üniversitesi Programlama Dilleri dersi kapsamında geliştirilmiş olup, kullanıcıdan alınan kodun **lexical ve syntax analizini** yaparak gerçek zamanlı olarak renklendiren (highlighting) bir grafik arayüz uygulamasıdır. Bu uygulamada, hazır hiçbir syntax renklendirme kütüphanesi kullanılmamış; **lexer, parser ve GUI sistemi tamamen sıfırdan** yazılmıştır.

---


### ✅ 1. Proje Planlaması ve Amaçların Belirlenmesi

Projenin hedefi, kod girişi yapan bir kullanıcı arayüzü ile birlikte:
- Kodun `token`’lara ayrılması (Lexical Analysis)
- Token’ların gramer kurallarına göre kontrol edilmesi (Syntax Analysis)
- Doğru yapıları farklı renklerle göstermek, hatalı yapıları vurgulamak

Belirli gramer kurallarına uygunluğu kontrol eden bir sistem kurulması amaçlandı:
```
statement → if (expr) block
statement → ID = expr ;
expr → ID | NUMBER | expr OP expr
block → { statement* }
```

---

### ✅ 2. Geliştirme Ortamının Kurulması

Projede:
- **Python ** (programlama dili)
- **Tkinter** (yerleşik GUI kütüphanesi)
- **VS Code** (kod editörü)

kullanılmıştır. Dış kütüphane veya modül eklenmemiştir.

---

### ✅ 3. Lexical Analyzer (Sözcüksel Çözümleyici)

Kod, karakter karakter okunarak token'lara ayrıldı. `re` (regex) kütüphanesi yerine tamamen elle ayıklama yöntemi kullanıldı.

```python
if c.isalpha() or c == "_":
    while i < len(code) and (code[i].isalnum() or code[i] == "_"):
        i += 1
    value = code[start:i]
    token_type = "KEYWORD" if value in self.keywords else "ID"
    tokens.append(Token(token_type, value, start, i))
```

Tanımlanan token türleri:
- `KEYWORD`, `ID`, `NUMBER`, `OP`, `SEPARATOR`, `MISMATCH`

---

### ✅ 4. Token Sınıfı Oluşturulması

Her token’ın tipi, değeri ve konumu tutulmuştur:

```python
class Token:
    def __init__(self, type, value, start_index, end_index):
        self.type = type
        self.value = value
        self.start_index = start_index
        self.end_index = end_index
```

Bu sayede GUI'de doğru konumda renklendirme yapılması mümkün hale gelmiştir.

---

### ✅ 5. Syntax Analyzer (Parser) Geliştirilmesi

Elle yazılmış bir **Top-Down Recursive Descent Parser** tasarlanmıştır. Kodun grammar kurallarına uyup uymadığı adım adım kontrol edilir.

```python
def statement(self):
    token = self.current()
    if token.value == "if":
        return self.if_statement()
    elif token.type == "ID":
        return self.assignment()
```

---

### ✅ 6. Expression (expr) ve Block Yapılarının Tanımı

İfadeler `expr()` ve `term()` fonksiyonlarıyla ayrıştırıldı. Karşılaştırmalı ve matematiksel ifadeler desteklenmiştir:

```python
def expr(self):
    if not self.term():
        return False
    while self.current() and self.current().type == "OP":
        self.index += 1
        if not self.term():
            return False
    return True
```

---

### ✅ 7. GUI Arayüzünün Oluşturulması

`Tkinter.Text` widget’ı kullanılarak kullanıcı arayüzü oluşturulmuştur. Yazılan kodlar anlık olarak analiz edilir.

```python
self.text = tk.Text(root, wrap="word", font=("Courier New", 12))
self.text.bind("<KeyRelease>", self.on_key_release)
```

---

### ✅ 8. Gerçek Zamanlı Renklendirme Sistemi

Her token türüne özel `tag` tanımlanmış ve GUI'de anlık olarak renklendirme yapılmıştır:

```python
self.text.tag_config("KEYWORD", foreground="blue")
self.text.tag_config("NUMBER", foreground="green")
self.text.tag_add(tag, start, end)
```

Hatalı yapılar kırmızı arka planla gösterilir:
```python
self.text.tag_config("ERROR", background="red", foreground="white")
```

---

### ✅ 9. Parser Hatalarının Görsel Vurgulanması

Eğer parser tüm token’ları işleyemezse, metnin tamamı hata olarak vurgulanır:

```python
parser = SyntaxAnalyzer(tokens)
parser.parse()
if parser.index < len(tokens):
    self.text.tag_add("ERROR", "1.0", "end")
```

---

### ✅ 10. Test, Genişletilebilirlik ve Teslim Süreci

Proje şu anda:
- `if`, `assignment`, `expr` yapılarını destekliyor
- `for`, `while` gibi yapılar ileride kolayca eklenebilir
- Kod sade, modüler ve genişlemeye açık olarak yazılmıştır

---

## 🧠 Sonuç

Bu proje, dil analizine dayalı uygulamalarda manuel lexer ve parser yazımının temellerini pratikte göstermektedir. `Tkinter` ile birleştirilerek kullanıcıya anlık geri bildirim veren işlevsel bir arayüz sunmaktadır.

---

## 👨‍💻 Geliştirici

**Fuat Üzülmez**  
23360859024  

---
