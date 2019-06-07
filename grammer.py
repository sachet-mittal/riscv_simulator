
from lark import Lark, Transformer, v_args

assembly_grammer = r"""
instruction: command|
             command operand|
             command operand "," operand|
             command operand "," operand "," operand

command: WORD
operand: [LETTER [NUMBER|LETTER]| SIGNED_INT]

%import common.DIGIT
%import common.SIGNED_INT
%import common.WORD
%import common.LETTER
%import common.NUMBER
"""


