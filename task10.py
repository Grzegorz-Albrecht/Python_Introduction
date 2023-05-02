n=int(input())
reshka=0
orel=0
for i in range(n):
    x=int(input())
    if x==0:
        reshka+=1
    else:
        orel+=1
if reshka>orel:
        print('orel',orel)
else:
     print('reshka',reshka)