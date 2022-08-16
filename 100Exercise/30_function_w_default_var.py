



def foo(b, a=2):
    return a + b

''' This is wrong: Non default has to be placed first, than the default one.

def foo(a=2, b):
    return a + b

'''