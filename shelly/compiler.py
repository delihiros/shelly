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

    def compile_list(ast, depth):
        first = ast.value[0]
        rest = ast.value[1:]

        if isinstance(first, sast.Symbol):
            if first.value == 'define':
                return
            elif first.value == 'defmacro':
                return
            elif first.value == 'if':
                return
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
            return

        return