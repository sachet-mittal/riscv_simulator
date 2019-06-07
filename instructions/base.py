
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
