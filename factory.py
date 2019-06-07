from instructions import *

def factory(class_name, *args):
    command = f"obj = {class_name} {args}"
    exec(command, globals())
    return obj

