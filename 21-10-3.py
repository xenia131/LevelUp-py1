dct_1 = {
    1: ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z'],
}
sums = 0
word = list(input().upper())


for i in word:
    for k, v in dct_1.items():
        if i in v:
            sums += k
print(sums)