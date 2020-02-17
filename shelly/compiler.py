import sast


class Compiler:
    def __init__(self):
        return

    def compile(self, ast, depth=0):
        shell = ''
        if isinstance(ast, sast.Program):
            for child in ast.value:
                shell += self.compile(child) + '\n'
        elif isinstance(ast, sast.Numeral):
            shell = str(ast.value)
        elif isinstance(ast, sast.String):
            shell = repr(ast.value)  # TODO: force double quote
        elif isinstance(ast, sast.Symbol):
            shell = ast.value
        elif isinstance(ast, sast.Expansion):
            shell = '${' + ast.value + '}'
        elif isinstance(ast, sast.List):
            shell = self.compile_list(ast, depth)
        return shell

    def compile_list(self, ast, depth):
        first = ast.value[0]
        rest = ast.value[1:]

        if isinstance(first, sast.Symbol):
            if first.value == 'define':
                token = self.compile(rest[0])
                value = self.compile(rest[1])
                if isinstance(rest[1], sast.List):
                    pass # need to expand and evaluate recursive
                return token + '=' + value + '\n'
            elif first.value == 'defmacro':
                return
            elif first.value == 'if':
                test = self.compile(rest[0])
                tru = self.compile(rest[1])
                fal = self.compile(rest[2])
                return 'if [ ' + test + ' ]; then\n' \
                        + tru \
                        + '\nelse\n' \
                        + fal \
                        + '\nfi\n'
            elif first.value == 'case':
                return
            elif first.value == 'while':
                return
            elif first.value == 'until':
                return
            elif first.value == 'for':
                return
            elif first.value == 'do':
                return
            elif first.value == 'and':
                return
            elif first.value == 'or':
                return
            elif first.value == 'not':
                return
            elif first.value == '!':
                return
            elif first.value == '+':
                return
            elif first.value == '-':
                return
            elif first.value == '*':
                return
            elif first.value == '/':
                return
            elif first.value == '<=':
                return
            elif first.value == '<':
                return
            elif first.value == '>=':
                return
            elif first.value == '>':
                return
            elif first.value == '|>':
                return
            elif first.value == '<|':
                return
            elif first.value == '=':
                return
            elif first.value == '!=':
                return
            elif first.value == 'cons':
                return
            elif first.value == 'first':
                return
            elif first.value == 'rest':
                return
            else:
                return self.compile(first) + ' ' \
                        + ' '.join([self.compile(option) for option in rest]) \
                        + '\n'
        return



def __main__():
    import tokenizer
    import parser
    t = tokenizer.Tokenizer()
    p = parser.Parser()
    c = Compiler()
    shelly = '(define hello\n  (ls -l))'
    tokens = t.tokenize('(hello\n  (option1)\n        option2 -l $HOME)')
    tokens = t.tokenize(shelly)
    print(shelly)
    asts = p.parse(tokens)
    print(asts)
    shell = c.compile(asts)
    print(shell)

if __name__ == '__main__':
    __main__()