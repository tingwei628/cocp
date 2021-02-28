import pytest
import pytest_check as check
import os
from cocp.lexer import cocp_lex_output


working_dir = os.path.dirname(os.path.abspath(__file__))

INPUT_TEST_CL_FILENAME = os.path.join(working_dir, 'lexer_input_test.cl')
COCP_LEXER_OUTPUT_FILENAME = os.path.join(working_dir, 'lexer_test_cocp_output.txt')
STD_LEXER_OUTPUT_FILENAME = os.path.join(working_dir, 'lexer_test_std_output.txt')



def setup():
  #print("SETUP")
  cocp_lex_output(INPUT_TEST_CL_FILENAME, COCP_LEXER_OUTPUT_FILENAME)
  pass

def test_test_cl(): 
  #compare output
  with open(COCP_LEXER_OUTPUT_FILENAME) as out_f:
    out_f_texts = out_f.readlines()
  with open(STD_LEXER_OUTPUT_FILENAME) as std_out_f:
    std_out_f_texts = std_out_f.readlines()
  i = 0
  std_out_len = len(std_out_f_texts)
  out_len = len(out_f_texts)
  
  check.equal(out_len, std_out_len)
  
  while i < std_out_len:
    check.equal(out_f_texts[i], std_out_f_texts[i])
    i+=1
    

  
"""
def test_1__lexer():
  x = 6
  assert x == 1, "failed"
  #passpass

"""
