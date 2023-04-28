a=int (input("Введите число: "))
S=0
while a>=1:
    S=a%10+S
    a=a//10
print(S)