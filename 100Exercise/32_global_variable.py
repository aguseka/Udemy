'''
Global varibale concept. Foo will produce 3
'''


c = 1
def foo():
    return c
c = 3
print(foo())