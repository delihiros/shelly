class AST:
    def __init__(self):
        return

    def __repr__(self):
        return ''.join(map(str, [self.__class__.__name__, ': ', self.value]))


class Program(AST):
    def __init__(self, value):
        self.value = value


class List(AST):
    def __init__(self, value):
        self.value = value


class String(AST):
    def __init__(self, value):
        self.value = value


class Numeral(AST):
    def __init__(self, value):
        self.value = value


class Expansion(AST):
    def __init__(self, value):
        self.value = value


class Symbol(AST):
    def __init__(self, value):
        self.value = value
