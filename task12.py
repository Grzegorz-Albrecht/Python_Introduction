S=int(input())
P=int(input())
for i in range(S):
    for j in range(P):
        if S==i+j and P==i*j:
            print(i,j)