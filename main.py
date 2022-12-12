# Scope - what variables do I have access to?
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)
outer()
'''
4 Consdierations
#1 - start with local variable

#2 - what is the parent local?

#3 - what are the global variables

#4 - consider built-in python functions
'''

