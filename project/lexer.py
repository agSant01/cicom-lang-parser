#
# GNU GENERAL PUBLIC LICENSE v2.0
#
# lexer.py
# Tokenizer for a lexeme and grammar for ICOM 4036 project
#
# @summary ply tokenizer/lexer
# @author Gabriel Santiago
#
#  Created at    : 2020-09-12 18:42:15
#
import ply.lex as lex
import argparse

reserved = {
    'in': 'IN',
    'if': 'IF',
    'let': 'LET',
    'empty': 'EMPTY',
    "cons": 'CONS',
    "first": 'FIRST',
    "rest": 'REST',
    "arity": 'ARITY',
    'then': 'THEN',
    'else': 'ELSE',
    'map': 'MAP',
    'to': 'TO',
    'true': 'TRUE',
    'false': 'FALSE',
    "number?": 'NUMBER_Q',
    "function?": 'FUNCTION_Q',
    "list?": 'LIST_Q',
    "empty?": 'EMPTY_Q',
    "cons?": 'CONS_Q',
}

tokens = list(reserved.values()) + [
    'EQ',
    'PLUS',
    'MINUS',
    'OPEN_PAREN',
    'CLOSE_PAREN',
    'SEMI_COLON',
    'COMMA',
    'OPERATOR',
    'DELIMITER',
    'CHARACTER',
    'DIGIT',
]


# reserved keywords
def t_NUMBER_Q(t):
    r'number\?'
    return t


def t_FUNCTION_Q(t):
    r'function\?'
    return t


def t_LIST_Q(t):
    r'list\?'
    return t


def t_EMPTY_Q(t):
    r'empty\?'
    return t


def t_CONS_Q(t):
    r'cons\?'
    return t


def t_EMPTY(t):
    r'empty'
    return t


def t_IF(t):
    r'if'
    return t


def t_THEN(t):
    r'then'
    return t


def t_ELSE(t):
    r'else'
    return t


def t_IN(t):
    r'in'
    return t


def t_LET(t):
    r'let'
    return t


def t_MAP(t):
    r'map'
    return t


def t_TO(t):
    r'to'
    return t


def t_TRUE(t):
    r'true'
    return t


def t_FALSE(t):
    r'false'
    return t


def t_CONS(t):
    r'cons'
    return t


def t_FIRST(t):
    r'first'
    return t


def t_REST(t):
    r'rest'
    return t


def t_ARITY(t):
    r'arity'
    return t


literals = ['~']


t_EQ = r':='
t_PLUS = r'\+'
t_MINUS = r'\-'

t_OPEN_PAREN = r'\('
t_CLOSE_PAREN = r'\)'

t_SEMI_COLON = r';'
t_COMMA = r','


t_OPERATOR = r'\*|/|==|!=|<=|>=|<|>|&|\|'
t_DELIMITER = r'\[|\]'
t_DIGIT = r'[0-9]'


def t_CHARACTER(t):
    r'[a-zA-Z]|\?|_'
    t.type = reserved.get(t.value, 'CHARACTER')
    return t


t_ignore = '\t\n '


# Error handling rule
def t_error(t):
    if t.value[0] in (' ', '\t', '\n'):
        # t.lexer.skip(1)
        print('whitespace')
        pass
    else:
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
        pass


# bulid lexer
lexer = lex.lex()

if __name__ == "__main__":
    lexer = lex.lex()
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("-i", "--input_path",
                            help="Completer file path of input file",
                            type=str,
                            required=True)

    args = arg_parser.parse_args()

    file_path = args.input_path

    with open(file_path, 'r') as file:

        lexer.input(file.read())
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(tok)
