import random
N=int(input())
k=int(input())
a=[random.randint(0,10) for x in range(N)]
print(a)
for i in a:
    if i==k or i==k-1 or i==k+1:
        print(i) 