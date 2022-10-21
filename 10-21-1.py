keys = list(input().split())
values = list(input().split())


dct = {}
for keys, values in zip(keys, values):
    dct[keys] = values

print(dct)