s = input("Введите строку :")
m = input("Введите символ :")
t=len(s) 
n = 0
for i in range(t):
    if s[i] == m:
        n +=1
print(n)
