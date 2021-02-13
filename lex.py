import sys
import ply.lex as lex
 # List of token names.   This is always required

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'fi': 'FI',
    'in': 'IN', 
    'class': 'CLASS',
    'Object': 'OBJECT_TYPE',
    'Main': 'MAIN_TYPE',
    'SELF_TYPE': 'SELF_TYPE',
    'String': 'STRING_TYPE',
    'Int': 'INT_TYPE',
    'Bool': 'BOOL_TYPE',
    'IO': 'IO_TYPE',
    'self': 'SELF',
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
    'not': 'NOT'
} 

tokens = [
    'INT_CONST',
    'STR_CONST',
    'BOOL_CONST',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'ID',
    'LE',
    'LESS',
    'GREATER',
    'GREATEREQUAL',
    'EQUAL',
    'SEMICOLON',
    'COMMA',
    'ASSIGN',
    'DISPATCH',
    'LBLOCK',
    'RBLOCK',
    'COLON',
    'LSQUAREBRACKET',
    'RSQUAREBRACKET',
    'DARROW',
    'AT',
    'INT_COMP'
] + list(reserved.values())

 # Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'\-'
t_TIMES   = r'\*'
t_DIVIDE  = r'\/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LE = r'\<\='
t_LESS = r'\<'
t_GREATER= r'\>'
t_GREATEREQUAL = r'\>\='
t_EQUAL = r'\='
t_DARROW = r'\=\>'
t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_ASSIGN = r'\<\-'
t_DISPATCH = r'\.'
t_LBLOCK = r'\{'
t_RBLOCK = r'\}'
t_COLON = r'\:'
t_LSQUAREBRACKET = r'\['
t_RSQUAREBRACKET = r'\]'
t_AT = r'\@'
t_INT_COMP = r'~'

# A regular expression rule with some action code
def t_INT_CONST(t):
 r'\d+'
 t.value = int(t.value)
 return t

# A string rule

def t_STR_CONST(t):
  r'\"([^\\\n|\r\n]|\\.)*?\"'
  return t

# bool rule
def t_BOOL_CONST(t):
  r'^(true|false)$'
  t.value 
  if t.value == 'true':
    t.value = True
  else:
    t.value = False
  return t


# Define a rule so we can track line numbers
def t_newline(t):
 r'\n+'
 t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t\f\r\v'

def t_COMMENT(t):
 r'(?:\(\*(?:(?!\*\))(.|\n|\r\n))*\*\)|\(\*[^\n|\r\n]*)'
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
