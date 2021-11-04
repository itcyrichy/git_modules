from functools import reduce

def multiply(*args):
    return reduce((lambda x,y:x*y),args)

def residue(a,b):
    return a%b