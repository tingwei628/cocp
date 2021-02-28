import sys
import ply.lex as lex
 # List of token names.   This is always required

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'fi': 'FI',
    'in': 'IN', 
    'class': 'CLASS',
    #'Object': 'OBJECT_TYPE',
    #'Main': 'MAIN_TYPE',
    #'SELF_TYPE': 'SELF_TYPE',
    #'String': 'STRING_TYPE',
    #'Int': 'INT_TYPE',
    #'Bool': 'BOOL_TYPE',
    #'IO': 'IO_TYPE',
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
    'TYPEID',
    'OBJECTID',
    'LE',
    'LESS',
    'GREATEREQUAL',
    'EQUAL',
    'SEMICOLON',
    'COMMA',
    'ASSIGN',
    'DISPATCH',
    'LBLOCK',
    'RBLOCK',
    'COLON',
    'DARROW',
    'AT',
    'INT_COMP',
    'ERROR'
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
t_AT = r'\@'
t_INT_COMP = r'~'


states = (
  ('COMMENT', 'exclusive'),       
)

t_COMMENT_ignore = ''

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
  #r'(?:\(\*(?:(?!\*\))(.|\n|\r\n))*\*\))'
  r'\(\*'
  t.lexer.code_start = t.lexer.lexpos
  t.lexer.comment_count = 1
  t.lexer.begin('COMMENT')


def t_begin_COMMENT(t):
  r'\(\*'
  t.lexer.comment_count += 1

def t_COMMENT_end(t):
  r'\*\)'
  t.lexer.comment_count -= 1 
  
  # unmatched *)
  if t.lexer.current_state() != 'COMMENT':
    return t_error(t)

  if t.lexer.comment_count == 0:
    t.value = t.lexer.lexdata[t.lexer.code_start: t.lexer.lexpos]
    #t.type = 'COMMENT'
    t.lexer.lineno += t.value.count('\n')
    t.lexer.lineno += t.value.count('\r\n')
    t.lexer.begin('INITIAL')

def t_TYPEID(t):
 r'[A-Z][a-zA-Z_0-9]*'
 t.type = reserved.get(t.value, 'TYPEID')
 return t

def t_OBJECTID(t):
 r'[a-zA-Z_][a-zA-Z_0-9]*'
 t.type = reserved.get(t.value, 'OBJECTID')
 return t

def t_COMMENT_error(t):
  last_pos = t.lexer.lexlen-1 
  t.lexer.skip(1)
  if t.lexer.current_state() == 'COMMENT' and last_pos == t.lexer.lexpos:
    t.type = 'ERROR'
    t.value = '\"EOF in comment\"'
    t.lineno += t.lexer.lexdata[t.lexer.code_start: t.lexer.lexpos].count('\n') + t.lexer.lexdata[t.lexer.code_start: t.lexer.lexpos].count('\r\n')+1
    return t


# Error handling rule
def t_error(t):
 t.type = 'ERROR'
 t.value = '\"{value}\"'.format(value=t.value[0])
 t.lexer.skip(1)
 return t


def cocp_lex(input_codes = ''):
  result = []
  # Build the lexer
  lexer = lex.lex()

  # Give the lexer some input
  lexer.input(input_codes)
  # Tokenize
  while True:
    tok = lexer.token()
    if not tok:
      break      # No more input
    result.append(tok)
    # print('#{tok_line} {tok_type} {tok_value}'.format(tok_line=tok.lineno, tok_type=tok.type, tok_value=tok.value))
  return result

def cocp_lex_output(input_filename=None, output_filename=None):
  input_codes = ''
  result = []
  with open(input_filename, 'r') as f:
    input_codes = f.read()
  
  result = cocp_lex(input_codes)
  with open(output_filename, 'w') as out_f:
    for tok in result:
      print('#{tok_line} {tok_type} {tok_value}'.format(tok_line=tok.lineno, tok_type=tok.type, tok_value=tok.value), file=out_f)

if __name__ == '__main__':
  with open(sys.argv[1],'r') as f:
    input_codes = f.read()
    cocp_lex(input_codes)
