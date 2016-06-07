#!/usr/bin/env python

from __future__ import print_function

import sys, os

# I hate how clumsy Python is here
dirname = os.path.join("..", os.path.dirname(__file__))
sys.path.append(dirname)

from py2_format import format_python2_stmts

for python2_stmts in (
          "import os.path",
#          "import os.path as path2",
#          "import os.path, dir.foo",
#         "exec 'exec-string' in locals, globals",
#         "exec 'exec-string' in dict",
#         "exec 'exec-string'",
#         "assert False",
#         "assert True, 'shit happens'",
#         "pass",
#         "pass; del x",
#         "global a, b, c, d",
#         "global a",
#         """if True:  pass
# """,
#         """if True:
#     pass

# """,
#         """
# if True:
#    pass
# else:
#    pass

# """,
#         """
# if True:
#    pass
# elif False:
#    pass

# """,
#         """
# if True:
#    pass
# elif False:
#    pass
# else:
#    pass

# """,
#         """
# if True:
#    if False:
#       del x
#    assert True
# elif False:
#    pass
# else:
#    import os
#    pass

# """,
        ):
    print(python2_stmts)
    print('-' * 30)
    formatted = format_python2_stmts(python2_stmts, show_tokens=True, showast=True, showgrammar=True)
    print(formatted)
    pass
