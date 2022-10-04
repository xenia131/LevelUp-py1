from calendar import c


def inp():
    a = int(input())
    b = int(input())
    st = input()
    return a, b, st
def math(a,b,st):
    if st == "+":
        print(a+b)
    elif st == "-":
        print(a-b)
    elif st == "*":
        print(a*b)
    else:
        print(a/b)
a, b, st = inp()
res = math(a,b,st)
