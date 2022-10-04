strs = [input() for i in range(int(input()))]
s = 0
for i in range(len(strs)):
    s += strs[i].count(' ')
print(s)