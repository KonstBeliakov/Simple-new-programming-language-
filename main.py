from lexer import *
from parser import Parser


def run(fn, text):
    # Generate tokens
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error:
        return None, error
    else:
        print(f'tokens: {tokens}')

    # Generate AST
    parser = Parser(tokens)
    ast = parser.parse()

    return ast, None


if __name__ == '__main__':
    while True:
        text = input('simple > ')
        result, error = run('<stdin>', text)

        if error:
            print(error.as_string())
        else:
            print(result)

