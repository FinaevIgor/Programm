s = input("Введите текст :")
t= len(s)
m = "."
n=0
for i in range(t):
    if s[i] == m:
        n += 1
print("В тексте",n,"предложений")