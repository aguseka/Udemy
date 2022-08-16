
'''
Thi is will throw name error

def foo():
    c = 1
    return c
foo()
print(c)


'''

''' This is not throwing error. Adding global will make c accessible by print'''

def foo():
    global c
    c = 1
    return c
foo()
print(c)

""" This is my original solution"""

def foo():
    c = 1
    return c
foo()
print(foo())