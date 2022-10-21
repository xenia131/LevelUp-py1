import re

def reading():
    return (input("calculate: "))


def calcs():
    eq = reading()
    eq_1 = re.split('-|\*|\+|/', eq)
    return eq_1
    
print(calcs())