import tokens
import sast


class ParseStream:
    def __init__(self, toks):
        self.toks = toks
        self.stream_length = len(self.toks)
        self.idx = 0
        self.first = self.toks[self.idx]
        self.rest = self.toks[self.idx + 1:]

    def next(self):
        self.idx += 1
        if self.idx >= self.stream_length:
            return None
        self.first = self.toks[self.idx]
        self.rest = self.toks[self.idx + 1:]
        return self.first


class Parser:
    def __init__(self):
        return

    def parse(self, toks):
        self.stream = ParseStream(toks)
        v = []
        while True:
            v.append(self.parse_stream())
            if len(self.stream.rest) == 0:
                break
        return sast.Program(v)

    def parse_stream(self):
        v = None
        if isinstance(self.stream.first, tokens.Brase):
            v = self.parse_list()
        elif isinstance(self.stream.first, tokens.Expansion):
            v = self.parse_expansion()
        elif isinstance(self.stream.first, tokens.Numeral):
            v = self.parse_numeral()
        elif isinstance(self.stream.first, tokens.Quote):
            v = self.parse_quote()
        elif isinstance(self.stream.first, tokens.String):
            v = self.parse_string()
        elif isinstance(self.stream.first, tokens.Symbol):
            v = self.parse_symbol()
        return v

    def parse_list(self):
        children = []
        brase = self.stream.first.tok
        self.stream.next()
        if brase == '(':
            while self.stream.first.tok != ')':
                v = self.parse_stream()
                children.append(v)
        elif brase == '[':
            while self.stream.first.tok != ']':
                v = self.parse_stream()
                children.append(v)
        elif brase == '{':
            while self.stream.first.tok != '}':
                v = self.parse_stream()
                children.append(v)
        self.stream.next()
        return sast.List(children)

    def parse_expansion(self):
        v = self.stream.first
        self.stream.next()
        return sast.Expansion(v.tok)

    def parse_numeral(self):
        v = self.stream.first
        self.stream.next()
        return sast.Numeral(v.tok)

    def parse_quote(self):
        return None

    def parse_string(self):
        v = self.stream.first
        self.stream.next()
        return sast.String(v.tok)

    def parse_symbol(self):
        v = self.stream.first
        self.stream.next()
        return sast.Symbol(v.tok)


def __main__():
    import tokenizer
    t = tokenizer.Tokenizer()
    p = Parser()
    tokens = t.tokenize('(hello\n  (option1)\n        option2 -l $HOME)')
    tokens = t.tokenize('(define hello\n  (ls -l))')
    asts = p.parse(tokens)
    print(asts)


if __name__ == '__main__':
    __main__()