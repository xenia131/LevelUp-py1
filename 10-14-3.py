symbs = [i for i in input()]
dct_1 = {}

for i in symbs:
    dct_1[i] = (symbs.count(i))

for i in dct_1:
    print(f"{i} : {dct_1[i]}")

