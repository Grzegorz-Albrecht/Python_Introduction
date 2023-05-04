# import random
# N=int(input())
# k=0
# a=[random.randint(0,10) for x in range(N)]
# print(a)
# for i in a:
#     if i==3:
#         k+=1
# if k!=0:        
#     print(k)        
# else: 
#     print('NO')        
import random
N=int(input())
k=int(input())
a=[random.randint(0,10) for x in range(N)]
print(a)
print(a.count(k))        
