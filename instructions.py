"""
Reference: https://rv8.io/isa.html
"""
class Instructions:
    def execute(self):
        raise NotImplementedError()

# TODO split into files and DRY these up
class ADD(Instructions):
    def __init__(self, destination, source1, source2):
        self.source1 = source1
        self.source2 = source2
        self.destination = destination

    def execute(self, memory, registers, pc):
        operand1 = registers[self.source1]
        operand2 = registers[self.source2]

        result = operand1 + operand2

        registers[self.destination] = result

        return pc + 1

class ADDI(ADD):
    def execute(self, memory, registers, pc):
        operand1 = registers[self.source1]
        operand2 = int(self.source2)

        result = operand1 + operand2

        registers[self.destination] = result

        return pc + 1

class SUB(Instructions):
    def __init__(self, destination, source1, source2):
        self.source1 = source1
        self.source2 = source2
        self.destination = destination

    def execute(self, memory, registers, pc):
        operand1 = registers[self.source1]
        operand2 = registers[self.source2]

        result = operand1 - operand2

        registers[self.destination] = result

        return pc + 1

class SUBI(SUB):
    def execute(self, memory, registers, pc):
        operand1 = registers[self.source1]
        operand2 = int(self.source2)

        result = operand1 - operand2

        registers[self.destination] = result

        return pc + 1

class AND(Instructions):
    def __init__(self, destination, source1, source2):
        self.source1 = source1
        self.source2 = source2
        self.destination = destination

    def execute(self, memory, registers, pc):
        operand1 = registers[self.source1]
        operand2 = registers[self.source2]

        result = operand1 & operand2

        registers[self.destination] = result

        return pc + 1

class ANDI(AND):
    def execute(self, memory, registers, pc):
        operand1 = registers[self.source1]
        operand2 = int(self.source2)

        result = operand1 & operand2

        registers[self.destination] = result

        return pc + 1


class OR(Instructions):
    def __init__(self, destination, source1, source2):
        self.source1 = source1
        self.source2 = source2
        self.destination = destination

    def execute(self, memory, registers, pc):
        operand1 = registers[self.source1]
        operand2 = registers[self.source2]

        result = operand1 | operand2

        registers[self.destination] = result

        return pc + 1

class ORI(OR):
    def execute(self, memory, registers, pc):
        operand1 = registers[self.source1]
        operand2 = int(self.source2)

        result = operand1 | operand2

        registers[self.destination] = result

        return pc + 1
class XOR(Instructions):
    def __init__(self, destination, source1, source2):
        self.source1 = source1
        self.source2 = source2
        self.destination = destination

    def execute(self, memory, registers, pc):
        operand1 = registers[self.source1]
        operand2 = registers[self.source2]

        result = operand1 ^ operand2

        registers[self.destination] = result

        return pc + 1

class XORI(XOR):
    def execute(self, memory, registers, pc):
        operand1 = registers[self.source1]
        operand2 = int(self.source2)

        result = operand1 ^ operand2

        registers[self.destination] = result

        return pc + 1

class XOR(Instructions):
    def __init__(self, destination, source1, source2):
        self.source1 = source1
        self.source2 = source2
        self.destination = destination

    def execute(self, memory, registers, pc):
        operand1 = registers[self.source1]
        operand2 = registers[self.source2]

        result = operand1 ^ operand2

        registers[self.destination] = result

        return pc + 1

class XORI(XOR):
    def execute(self, memory, registers, pc):
        operand1 = registers[self.source1]
        operand2 = int(self.source2)

        result = operand1 ^ operand2

        registers[self.destination] = result

        return pc + 1

class LUI(Instructions):
    def __init__(self, destination, immediate):
        self.destination = destination
        self.immediate = immediate

    def execute(self, memory, registers, pc):
        registers[self.destination] = int(self.immediate)
        return pc + 1

class AUIPC(Instructions):
    def __init__(self, destination, offset):
        self.destination = destination
        self.offset = offset

    def execute(self, memory, registers, pc):
        registers[self.destination] = pc + int(self.offset)
        return pc + 1

class JAL(Instructions):
    def __init__(self, destination, offset):
        self.destination = destination
        self.offset = int(offset)

    def execute(self, memory, registers, pc):
        registers[self.destination] = pc + 1
        return pc + self.offset

class JALR(Instructions):
    def __init__(self, destination, source1, offset):
        self.source1 = source1
        self.destination = destination
        self.offset = int(offset)

    # TODO come back to this
    def execute(self, memory, registers, pc):
        s1 = registers[self.source1]
        registers[self.destination] = pc + 1
        pc = (s1 + self.offset) ** -2
        return pc

class BEQ(Instructions):
    def __init__(self, source1, source2, offset):
        self.source1 = source1
        self.source2 = source2
        self.offset = int(offset)

    def execute(self, memory, registers, pc):
        operand1 = registers[self.source1]
        operand2 = registers[self.source2]

        if operand1 == operand2:
            return pc + self.offset 

        return pc + 1


class BNE(Instructions):
    def __init__(self, source1, source2, offset):
        self.source1 = source1
        self.source2 = source2
        self.offset = int(offset)

    def execute(self, memory, registers, pc):
        operand1 = registers[self.source1]
        operand2 = registers[self.source2]

        if operand1 != operand2:
            return pc + self.offset 

        return pc + 1

class BLT(Instructions):
    def __init__(self, source1, source2, offset):
        self.source1 = source1
        self.source2 = source2
        self.offset = int(offset)

    def execute(self, memory, registers, pc):
        operand1 = registers[self.source1]
        operand2 = registers[self.source2]

        if operand1 < operand2:
            return pc + self.offset 

        return pc + 1

class BGE(Instructions):
    def __init__(self, source1, source2, offset):
        self.source1 = source1
        self.source2 = source2
        self.offset = int(offset)

    def execute(self, memory, registers, pc):
        operand1 = registers[self.source1]
        operand2 = registers[self.source2]

        if operand1 >= operand2:
            return pc + self.offset 

        return pc + 1


class LB(Instructions):
    def __init__(self, destination, source1, offset):
        self.source1 = source1
        self.destination = destination
        self.offset = int(offset)

    def execute(self, memory, registers, pc):
        location = self.source1 + self.offset
        data = memory[location]
        data = int(data, 2)
        registers[self.destination] = data
        return pc + 1

class LH(Instructions):
    def __init__(self, destination, source1, offset):
        self.source1 = source1
        self.destination = destination
        self.offset = int(offset)

    def execute(self, memory, registers, pc):
        location = self.source1 + self.offset
        data = memory[location] + memory[location + 1]
        data = int(data, 2)
        registers[self.destination] = data
        return pc + 1

class LW(Instructions):
    def __init__(self, destination, source1, offset):
        self.source1 = source1
        self.destination = destination
        self.offset = int(offset)

    def execute(self, memory, registers, pc):
        location = self.source1 + self.offset
        data = memory[location] + memory[location + 1] + \
                memory[location + 2] + memory[location + 3]
        data = int(data, 2)
        registers[self.destination] = data
        return pc + 1


class SB(Instructions): 
    def __init__(self, source1, destination, offset):
        self.source1 = source1
        self.destination = destination
        self.offset = int(offset)

    def execute(self,  memory, registers, pc):
        data = registers[self.source1]
        location = self.destination + self.offset
        
        # Formatting data
        data = bin(data)[2:][-8:]
        data = f"{data:>08}"

        memory[memory] = data

        return pc + 1


class SH(Instructions): 
    def __init__(self, source1, destination, offset):
        self.source1 = source1
        self.destination = destination
        self.offset = int(offset)

    def execute(self,  memory, registers, pc):
        data = registers[self.source1]
        location = self.destination + self.offset
        
        # Formatting data
        data = bin(data)[2:][-16:]
        data = f"{data:>016}"

        memory[memory] = data[:8]
        memory[memory + 1] = data[8:16]

        return pc + 1


class SW(Instructions): 
    def __init__(self, source1, destination, offset):
        self.source1 = source1
        self.destination = destination
        self.offset = int(offset)

    def execute(self,  memory, registers, pc):
        data = registers[self.source1]
        location = self.destination + self.offset
        
        # Formatting data
        data = bin(data)[2:][-32:]
        data = f"{data:>032}"

        memory[memory] = data[:8]
        memory[memory + 1] = data[8:16]
        memory[memory + 2] = data[16:24]
        memory[memory + 3] = data[24:]

        return pc + 1

class SLT(Instructions): 
    def __init__(self, destination, source1, source2):
        self.source1 = source1
        self.source2 = source2
        self.destination = destination

    def execute(self,  memory, registers, pc):
        operand1 = registers[self.source1]
        operand2 = registers[self.source2]
        if operand1 < operand2:
            registers[self.destination] = 1
        return pc + 1

class SLTI(Instructions): 
    def __init__(self, destination, source1, immediate):
        self.source1 = source1
        self.destination = destination
        self.immediate = int(immediate)

    def execute(self,  memory, registers, pc):
        operand1 = registers[self.source1]
        operand2 = immediate
        if operand1 < operand2:
            registers[self.destination] = 1
        return pc + 1

class SLL(Instructions): 
    def __init__(self, destination, source1, source2):
        self.source1 = source1
        self.source2 = source2
        self.destination = destination

    def execute(self,  memory, registers, pc):
        n = registers[self.source1]
        n = bin(n)[2:]
        n = n.rjust(32, "0")

        shift_by = registers[self.source2]

        result = n[shift_by:] + "0" * shift_by
        registers[self.destination]  = int(result, 2)

        return pc + 1


class SLLI(Instructions): 
    def __init__(self, destination, source1, immediate):
        self.source1 = source1
        self.destination = destination
        self.immediate = int(immediate)

    def execute(self,  memory, registers, pc):
        n = registers[self.source1]
        n = bin(n)[2:]
        n = n.rjust(32, "0")

        shift_by = self.immediate

        result = n[shift_by:] + "0" * shift_by
        registers[self.destination]  = int(result, 2)

        return pc + 1

class SRLI(Instructions): 
    def __init__(self, destination, source1, immediate):
        self.source1 = source1
        self.destination = destination
        self.immediate = int(immediate)

    def execute(self,  memory, registers, pc):
        n = registers[self.source1]
        n = bin(n)[2:]
        n = n.rjust(32, "0")

        shift_by = self.immediate

        result = "0" * shift_by + n[:-shift_by]

        registers[self.destination]  = int(result, 2)

        return pc + 1

class SRAI(Instructions): 
    def __init__(self, destination, source1, immediate):
        self.source1 = source1
        self.destination = destination
        self.immediate = int(immediate)

    def execute(self,  memory, registers, pc):
        n = registers[self.source1]
        shift_by = self.immediate


        registers[self.destination]  = n >> shift_by 

        return pc + 1

class SRA(Instructions): 
    def __init__(self, destination, source1, source2):
        self.source1 = source1
        self.source2 = source2
        self.destination = destination

    def execute(self,  memory, registers, pc):
        n = registers[self.source1]
        shift_by = registers[self.source2]


        registers[self.destination]  = n >> shift_by 

        return pc + 1

"""
SRL
"""
class SLTU(Instructions):pass
class SLTIU(Instructions):pass
class BGEU(Instructions): pass
class BLTU(Instructions): pass
class LBU(Instructions): pass
class LHU(Instructions): pass
