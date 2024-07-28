class Exp:
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent

class Reader:
    def __init__(self, text):
        self.text = text

code = '''

x = 1

'''

r = Reader(code)
print(r.text)