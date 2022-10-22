import tokenize
import io 
expr = []
inp =  input()
for t in tokenize.tokenize(io.BytesIO(bytes(inp, "utf-8")).readline):
    if t.type in [2,54]:
        expr.append(t.string)

print(expr) 