month = int(input())
list1 = [1,3,5,7,8,10,12]
list2 = [4,6,9,11]
if month in list1:
    print("31")
elif month in list2:
    print("30")
else:
    print("FEBRUARY!")