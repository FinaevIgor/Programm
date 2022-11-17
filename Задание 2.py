from random import randint
x=[]
n= 10
num = [randint(-100, 100) for i in range(n)]
x.append(num)
print ("Список: " +  str(num))
a = max(num)
print("максимальное число: ", a)
b = min(num)
print("минимальное число: ", b)
i = 0
print('cумма положительных чисел:', sum(i > 0 for i in num))
print('сумма отрицательных чисел:', sum(i < 0 for i in num))