import memory
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
    while pc != len(machine_code):
        pc = machine_code[pc].execute(main_memory, register_file, pc)

def main():
    f = "test/multiply.txt"
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
