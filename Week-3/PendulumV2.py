import math
print(math.pi) # Math Imported giving access to math functions
def period(g,l):
    if isinstance(g, str) or isinstance(l, str):  # creates a boolean if true raises error
        raise TypeError
    if (g<=0) or (L=0):
        raise ValueError
    equation = 2*pi * math.sqrt(g/L)
    return equation