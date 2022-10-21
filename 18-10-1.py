import random
from timeit import timeit

def dice():
    return (random.randint(1, 6) + random.randint(1, 6))

dct_1 = {i: 0 for i in range(2,13)}
#print(dct_1)
for i in range(500):
    a = dice()
    dct_1[a] += 1
for k,v in dct_1.items():
    dct_1[k] = v/10

print(dct_1)