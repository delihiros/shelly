class AST:
    def __init__(self):
        return

    def __repr__(self):
        return ''.join(map(str, [self.__class__.__name__, ': ', self.value]))


class List(AST):
    def __init__(self, value):
        self.value = value


class String(AST):
    def __init__(self, value):
        self.value = value