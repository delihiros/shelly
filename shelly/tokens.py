class Tokens:
    def __init__(self):
        return

    def __repr__(self):
        return ''.join(map(str, [self.__class__.__name__, ': ', self.tok]))


class Brases(Tokens):
    def __init__(self, tok):
        self.tok = tok


class Numeral(Tokens):
    def __init__(self, tok):
        self.tok = tok


class Symbol(Tokens):
    def __init__(self, tok):
        self.tok = tok