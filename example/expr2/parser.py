#  Copyright (c) 2016 Rocky Bernstein
"""
More complex expression parsing
"""

from __future__ import print_function

import sys
from spark_parser.ast import AST

from scanner import ExprScanner

from spark_parser import GenericASTBuilder, DEFAULT_DEBUG

class ExprParser(GenericASTBuilder):
    """A more complete expression Parser.

    Note: function parse() comes from GenericASTBuilder
    """

    def __init__(self, debug=DEFAULT_DEBUG):
        super(ExprParser, self).__init__(AST, 'expr', debug=debug)
        self.debug = debug

    def nonterminal(self, nt, args):
        collect = ()

        has_len = hasattr(args, '__len__')
        if nt in collect and len(args) > 1:
            #
            #  Collect iterated thingies together.
            #
            rv = args[0]
            rv.append(args[1])
        elif (has_len and len(args) == 1 and
              hasattr(args[0], '__len__') and len(args[0]) == 1):
            # Remove singleton derivations
            rv = GenericASTBuilder.nonterminal(self, nt, args[0])
            del args[0] # save memory
        else:
            rv = GenericASTBuilder.nonterminal(self, nt, args)
        return rv

    ##########################################################
    # Python 2 grammar rules. Grammar rule functions
    # start with the name p_ and are collected automatically
    ##########################################################
    def p_expr(self, args):
        '''
        expr       ::= expr BITOP shift_expr
        expr       ::= shift_expr
        shift_expr ::= shift_expr ARITH_OP arith_expr
        shift_expr ::= arith_expr
        arith_expr ::= arith_expr ADD_OP term
        arith_expr ::= term
        term       ::= term MULT_OP factor
        term       ::= factor
        factor     ::= UNARY_OP factor
        factor     ::= atom
        atom       ::= NUMBER
        atom       ::= LPAREN expr RPAREN
        NUMBER     ::= INTEGER
        # Add this when we want to handle type checking.
        # NUMBER     ::= INTEGER DOT INTEGER
        '''

def parse_python(python_str, out=sys.stdout,
                 show_tokens=False, parser_debug=DEFAULT_DEBUG):
    assert isinstance(python_str, str)
    tokens = ExprScanner().tokenize(python_str)
    for t in tokens:
        print(t)

    # For heavy grammar debugging
    # parser_debug = {'rules': True, 'transition': True, 'reduce': True,
    #                 'errorstack': True}
    parser_debug = {'rules': False, 'transition': False, 'reduce': True,
                    'errorstack': True}
    return ExprParser(parser_debug).parse(tokens)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        expression = "(1 + 3)/2"
    else:
        expression = " ".join(sys.argv[1:])
    ast = parse_python(expression, show_tokens=True)
    print(ast)
