dct_1 = {
    1: ['.',',','?','!',':'],
    2: ['A', 'B', 'C'],
    3: ['D', 'E', 'F'],
    4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'],
    6: ['M', 'N', 'O'],
    7: ['P', 'Q', 'R', 'S'],
    8: ['T', 'U', 'V'],
    9: ['W', 'X', 'Y', 'Z'],
    0: [' ']
}

def text(n, m):
    let = dct_1[m]
    n -= 1
    l = len(let)
    return let[n % l]
    
n = int(input())
m = [input().split() for i in range(int(input())-1)]

print(text(n,m))
