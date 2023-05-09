import random 
N=int(input('Введите размер массива: '))
min_number = int(input('Введите минимум диапазона: '))
max_number = int(input('Введите максимум диапазона: '))
a=[random.randint(0,1000) for x in range(N)]
print(a)
for i in range(N):
    if min_number<=a[i]<=max_number:
        print('Число:',a[i],'Индекс:',i)