import tokens


def is_special_char(c):
    return c in '#$&|<>-+*/%!?=~^\\_@;:,.'


def is_quote(c):
    return c in '"\'`'


def is_smallalpha(c):
    return 'a' <= c and c <= 'z'


def is_bigalpha(c):
    return 'A' <= c and c <= 'Z'


def is_num(c):
    return '0' <= c and c <= '9'


def is_space(c):
    return c in ' \t\n'


def is_brase(c):
    return c in '()[]{}'


class Tokenizer:
    def __init__(self):
        return

    def tokenize(self, string):
        index, max_index = 0, len(string)
        toks = []
        while index < max_index:
            while index < max_index and is_space(string[index]):
                index += 1

            if is_brase(string[index]):
                toks.append(tokens.Brase(string[index]))
                index += 1
            elif is_num(string[index]):
                num = ''
                while index < max_index and is_num(string[index]):
                    num += string[index]
                    index += 1
                toks.append(tokens.Numeral(num))
            elif is_smallalpha(string[index]) or is_bigalpha(string[index]) or is_special_char(string[index]):
                sym = ''
                if string[index] == '$':
                    while index < max_index and not is_space(string[index]) and string[index] not in '()[]':
                        sym += string[index]
                        index += 1
                    sym = sym.strip('$').strip('{').rstrip('}')
                    toks.append(tokens.Expansion(sym))
                else:
                    while index < max_index and is_smallalpha(string[index]) or is_bigalpha(string[index]) or is_num(string[index]) or is_special_char(string[index]):
                        sym += string[index]
                        index += 1
                    toks.append(tokens.Symbol(sym))
            elif is_quote(string[index]):
                starting_quote = string[index]
                if starting_quote == '"':
                    s = ''
                    index += 1
                    while index < max_index and string[index] != starting_quote:
                        s += string[index]
                        index += 1
                    index += 1
                    toks.append(tokens.String(s))

        return toks


def __main__():
    tokenizer = Tokenizer()
    print(tokenizer.tokenize('123'))
    print(tokenizer.tokenize('(123)'))
    print(tokenizer.tokenize('(function param1 param2)'))
    print(tokenizer.tokenize('(if (= str1 str2) hello world)'))
    print(tokenizer.tokenize('((wow) "hello word")'))
    print(tokenizer.tokenize('(hello\n  (option1)\n        option2 -l)'))
    print(tokenizer.tokenize('${HOME}'))
    print(tokenizer.tokenize('(hello ${LC_CTYPE})'))


if __name__ == '__main__':
    __main__()