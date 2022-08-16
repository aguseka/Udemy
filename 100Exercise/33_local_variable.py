''' Local variable concept. Foo will broduce 2'''

c = 1
def foo():
    c = 2
    return c
c = 3
print(foo())
