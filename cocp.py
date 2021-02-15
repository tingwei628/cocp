import sys
from lexer import cocp_lex

def compile(input_code = ''):
  #lex
  toks = cocp_lex(input_code)
  #parse
  #semantic analyze
  #optimize
  #codegen


if __name__ == '__main__':
  print('=== COCP start to compile ===')
  input_code = ''
  with open(sys.argv[1],'r') as f:
    input_code = f.read()
  compile(input_code)
