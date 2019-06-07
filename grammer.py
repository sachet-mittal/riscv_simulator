from factory import factory
from lark import Lark, Transformer, v_args

#import lark.lexer.Token as Token
from lark.lexer import Token

assembly_grammer = r"""
?instruction: command
            |command WS operand
            |command WS operand "," WS operand
            |command WS operand "," WS operand "," WS operand

command: WORD 
operand: [LETTER [NUMBER|LETTER]| SIGNED_INT]

%import common.SIGNED_INT
%import common.WORD
%import common.LETTER
%import common.NUMBER
%import common.WS
"""
#parser.parse("Add")
#
class AssemblyTransformer(Transformer): 
    @v_args(inline=True)
    def command(self, items):
        return items[:].upper()

    @v_args(inline=True)
    def operand(self, *items):
        return "".join(items)

    def instruction(self, items):
        items = [x for x in items if not isinstance(x, Token)] # Ignore WS 
        operation = items[0]
        operands = items[1:]
        return factory(operation, *operands)

lexer = Lark(assembly_grammer,parser="lalr", start="instruction")

transformer = AssemblyTransformer()

tokenized = lexer.parse("Add r1, r2, -2")
ast = AssemblyTransformer().transform(tokenized)
# transformer.parse("Add r1, r2, r3")


