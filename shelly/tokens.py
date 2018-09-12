class Token:
    def __init__(self):
        return

    def __repr__(self):
        return ''.join(map(str, [self.__class__.__name__, ': ', self.tok]))


class Quote(Token):
    def __init__(self, tok):
        self.tok = tok


class Brase(Token):
    def __init__(self, tok):
        self.tok = tok


class Numeral(Token):
    def __init__(self, tok):
        self.tok = tok


class String(Token):
    def __init__(self, tok):
        self.tok = tok


class Symbol(Token):
    def __init__(self, tok):
        self.tok = tok


class Expansion(Token):
    def __init__(self, tok):
        self.tok = tok