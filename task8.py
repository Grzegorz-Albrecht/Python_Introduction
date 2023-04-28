m=int(input())
n=int(input())
k=int(input())
if k>=n and k//n<m and k%n==0:
    print("YES")
else:
    print("NO")