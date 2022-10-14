def sort(list):
    list = [input() for i in range(int(input()))]
    return list == sorted(list) or list == reversed(list)

print(sort(list))