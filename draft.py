a = [input() for i in range(int(input()))]
q = []
even = []
#a = [int(x) for x in input().split()]
for i in range(len(a)):
    t = int(a[i])
    q += [t*t]
    if t%2 ==0:
        even += [t]
print(q, even, sep = '\n')
