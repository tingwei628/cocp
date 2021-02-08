import sys
import ply.lex as lex
 # List of token names.   This is always required
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'ID'
)


reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'fi': 'FI',
    'in': 'IN', 
    'class': 'CLASS',
    'inherits': 'INHERITS',
    'let': 'LET',
    'loop': 'LOOP',
    'pool': 'POOL',
    'then': 'THEN',
    'while': 'WHILE',
    'case': 'CASE',
    'esac': 'ESAC',
    'of': 'OF',
    'new': 'NEW',
    'isvoid': 'ISVOID',
    'not': 'NOT',
    'true': 'TRUE',
    'false': 'FALSE' 
} 

 # Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'


# A regular expression rule with some action code
def t_NUMBER(t):
 r'\d+'
 t.value = int(t.value)
 return t

# Define a rule so we can track line numbers
def t_newline(t):
 r'\n+'
 t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def t_COMMENT(t):
 r'(?:\(\*(?:(?!\*\))(.|\n|\r\n))*\*\))'
 pass

def t_ID(t):
 r'[a-zA-Z_][a-zA-Z_0-9]*'
 t.type = reserved.get(t.value, 'ID')
 return t

# Error handling rule
def t_error(t):
 print("Illegal character '%s'" % t.value[0])
 t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
with open(sys.argv[1],'r') as f:
    data = f.read()
# Test it out
"""
data = '''
3 + 4 * 10
+ -20 *2
'''
"""

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
 tok = lexer.token()
 if not tok:
     break      # No more input
 print(tok)


if __name__ == '__main__':
  r"\\"
