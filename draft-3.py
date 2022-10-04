def deposit():
    size = int(input())
    term = int(input())
    percent = float(input())
    return size*(1+(term*percent)/100)
sum = deposit()
print(sum)