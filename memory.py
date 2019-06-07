
class PartialFrozenDict(dict):
    def __init__(self, *args, **kargs):
        self.frozen_keys = kwargs.pop("frozen", [])
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if key in self.frozen_keys:
            return
        return super().__setitem__(key, value)

def initialize_main_memory(byte_count=1000):
    memory = {i: "{0:08b}".format(0) for i in range(byte_count)}
    return memory

def initialize_registers(count=32):
    regs = {f"r{i}": 0 for i in range(count)}
    return regs
