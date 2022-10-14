def sort(list):
    list = [input() for i in range(int(input()))]
    if list == sorted(list):
        return True
    else: 
        return False

print(sort(list))