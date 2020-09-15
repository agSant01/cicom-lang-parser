#
# GNU GENERAL PUBLIC LICENSE v2.0
#
# parser.py
#
# @summary ply parser
# @author Gabriel Santiago
#
# Created at    : 2020-09-12 18:42:15
#
from .lexer import tokens, reserved
import argparse
import ply.yacc as yacc


def p_exp(p):
    '''
    exp : term binop exp
        | term 
        | IF exp THEN exp ELSE exp
        | LET def IN exp
        | MAP idlist TO exp
    '''


def p_term(p):
    '''
    term : unop term
         | factor OPEN_PAREN explist CLOSE_PAREN
         | factor
         | bool
         | int
         | empty
    '''


def p_factor(p):
    '''
    factor : OPEN_PAREN exp CLOSE_PAREN
           | prim
           | id 
    '''


def p_def(p):
    '''
    def : id EQ exp SEMI_COLON def
        | id EQ exp SEMI_COLON
    '''


def p_explist(p):
    '''
    explist : propexplist 
            | 
    '''


def p_propexplist(p):
    '''
    propexplist : exp COMMA propexplist
                | exp 
    '''


def p_idlist(p):
    '''
    idlist : propidlist
           | 
    '''


def p_prop_idlist(p):
    '''
    propidlist : id COMMA propidlist
               | id
    '''


def p_bool(p):
    '''
    bool : FALSE
         | TRUE
    '''


def p_sign(p):
    '''
    sign : PLUS
         | MINUS
    '''


def p_unop(p):
    '''
    unop : sign 
         | '~'
    '''


def p_binop(p):
    '''
    binop : sign 
          | OPERATOR
    '''


def p_prim(p):
    '''
    prim : NUMBER_Q 
         | CONS_Q
         | EMPTY_Q
         | FUNCTION_Q
         | LIST_Q
         | ARITY
         | CONS 
         | DELIMITER
         | FIRST
         | REST
    '''


def p_id(p):
    '''
    id : id DIGIT
       | id CHARACTER
       | CHARACTER
    '''


def p_int_digit(p):
    '''
    int : int DIGIT
        | DIGIT
    '''


def p_empty(p):
    '''
    empty : EMPTY
    '''


def p_error(p):
    if p:
        raise Exception(
            f'PARSE ERROR in TOKEN: {p.type} CHARACTER: {p.value} LINE: {p.lineno} COLUMN: {p.lexpos}')
    else:
        # EOF error means that the gramar is not complete
        raise Exception(
            'EOF ERROR. Syntax is not complete.')


parser = yacc.yacc(write_tables=False, outputdir='./out', debug=True)

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("-i", "--input_path",
                            help="Completer file path of input file",
                            type=str,
                            required=True)

    args = arg_parser.parse_args()

    file_path = args.input_path

    with open(file_path, 'r') as file:
        parser.parse(file.read())
