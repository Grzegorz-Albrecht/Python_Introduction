import random
N=int(input())
a=[random.randint(0,100) for x in range(N)]
Max=0
S=0
print(a)
for i in range(N):
    if i==N-1:
        S=a[i]+a[i-1]+a[0]
        print(S)
        if S>Max:
            Max=S
    else:    
        S=a[i]+a[i-1]+a[i+1]
        i+=1
        print(S)
        if S>Max:
            Max=S
print('Max',Max)