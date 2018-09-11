import tokens


def is_smallalpha(c):
    return 'a' <= c and c <= 'z'


def is_bigalpha(c):
    return 'A' <= c and c <= 'Z'


def is_num(c):
    return '0' <= c and c <= '9'


def is_space(c):
    return ' ' == c or '\t' == c


class Tokenizer:
    def __init__(self):
        return

    def tokenize(self, string):
        index, max_index = 0, len(string)
        toks = []
        while index < max_index:
            while index < max_index and is_space(string[index]):
                index += 1

            if string[index] in ['(', ')', '[', ']', '{', '}']:
                toks.append(tokens.Brases(string[index]))
                index += 1
            elif is_num(string[index]):
                num = ''
                while index < max_index and is_num(string[index]):
                    num += string[index]
                    index += 1
                toks.append(tokens.Numeral(num))
            elif is_smallalpha(string[index]) or is_bigalpha(string[index]):
                sym = ''
                while index < max_index and is_smallalpha(string[index]) or is_bigalpha(string[index]) or is_num(string[index]):
                    sym += string[index]
                    index += 1
                toks.append(tokens.Symbol(sym))
        return toks


def __main__():
    tokenizer = Tokenizer()
    print(tokenizer.tokenize('123'))
    print(tokenizer.tokenize('(123)'))
    print(tokenizer.tokenize('(function param1 param2)'))


if __name__ == '__main__':
    __main__()