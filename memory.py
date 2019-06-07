
def initialize_memory(byte_count=1000):
    memory = {i: "{0:08b}".format(0) for i in range(byte_count)}
    return memory

def initialize_registers(count=32):
    regs = {f"r{i}": 0 for i in range(count)}
    return regs
