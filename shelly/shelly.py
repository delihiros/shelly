import argparse
import sys
import tokenizer
import parser
import compiler


class Shelly:
    def __init__(self):
        self.t = tokenizer.Tokenizer()
        self.p = parser.Parser()
        self.c = compiler.Compiler()

    def generate(self, s):
        tokens = self.t.tokenize(s)
        ast = self.p.parse(tokens)
        shell_script = self.c.compile(ast)
        return shell_script

    def from_file(self, f):
        s = ''.join([line for line in f])
        return self.generate(s)


def __main__():
    parser = argparse.ArgumentParser(
        description='compiles Lisp to Shell Script')
    parser.add_argument('infile', action='store', nargs='?',
                        type=argparse.FileType('r'), default=sys.stdin)
    args = parser.parse_args()
    shelly = Shelly()
    shell_script = shelly.from_file(args.infile)
    print(shell_script)


if __name__ == '__main__':
    __main__()
