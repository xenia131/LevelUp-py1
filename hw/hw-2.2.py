import statistics as st
my_list = [input() for i in range(int(input()))]

def mean(my_list):
    sum = 0
    for i in range(len(my_list)):
        sum += float(my_list[i])
    mean_number = sum / (i+1)
    return mean_number

print(f"a. min number: {min(my_list)},\nb. max number: {max(my_list)},\nc. mean number: {mean(my_list)},\nd. sorted list: {sorted(my_list)}")
