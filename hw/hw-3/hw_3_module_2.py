import re
import tokenize
import io 

def reading():
    return (input("calculate: "))

def calcs():
    calc = []
    inp =  reading()
    for t in tokenize.tokenize(io.BytesIO(bytes(inp, "utf-8")).readline):
        if t.type in [2,54]:
            calc.append(t.string)
    return calc
    

#print(calcs())