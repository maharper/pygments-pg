# from pygments.lexers.perl import PerlLexer, 
from pygments.lexer import  words, inherit
from pygments.lexers.perl import PerlLexer
from pygments.token import *
# from pygments.token import Name, Keyword

__all__ = ['PGLexer']

class PGLexer(PerlLexer):
    name = 'PG'
    aliases = ['pg']
    filenames = ['*.pg']


    tokens = {
        'root': [
            (words(('test-token-1','test-token-2',), suffix=r'\b'), Name.Builtin),
            inherit,
        ],
    }
