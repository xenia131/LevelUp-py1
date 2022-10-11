'''Напишите программу, которая будет запрашивать у пользователя длины всех трех сторон треугольника и выдавать сообщение о том, к какому
типу следует его относить. (Равносторонний, равнобедренный, разносторонний)
'''
a = float(input("print side-a: "))
b = float(input("print side b: "))
c = float(input("print side c: "))

res = {(a == b == c): 'equilateral triangle',
       (a == b != c or a != b == c): 'isosceles triangle',
       (a != b != c): 'random triangle',
       (a <=0 or b <= 0 or c <=0): 'error triangle'}[True]
print(res)