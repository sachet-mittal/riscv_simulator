import memory
import sys
from grammer import lexer, transformer

def create_environment():
    main_memory = memory.initialize_main_memory()
    gen_register = memory.initialize_registers()
    return main_memory, gen_register

def lex(filename):
    tokens = []
    with open(filename) as f:
        lines = [line.strip() for line in f]
    for line in lines:
        tokenized = lexer.parse(line)
        tokens.append(tokenized)
    return tokens

def transform(tokens):
    asts = []
    for token in tokens:
        ast = transformer.transform(token)
        asts.append(ast)
    return asts

def execute(main_memory, register_file, machine_code, pc):
    print ("Executing...")
    while pc != len(machine_code):
        instruction = machine_code[pc]
        print (instruction)
        pc = instruction.execute(main_memory, register_file, pc)

def main():
    #parser = argparse.ArgumentParser()
    #parser.add_argument("-i", "--input", help="A text file which is the assembly code", action=)
    #args = parser.parse_args()

    f = sys.argv[1]
    print ("executing file %s", f)
    # Set up Virtual Environment
    memory_file, register_file = create_environment()    

    pc = 0 # Execution starts form first line
    
    # generate stream of tokens
    tokens = lex(f)

    # Create ASTS
    transformed = transform(tokens)

    # Exectute in the virtual environment
    execute(memory_file, register_file, transformed, pc)
    import pdb; pdb.set_trace()

if __name__ == "__main__":
    main()
