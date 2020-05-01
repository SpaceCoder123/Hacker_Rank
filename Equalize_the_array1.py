N=int(input())
L=list(map(int,input().split()))
C=[]
for i in L:
    C.append(L.count(i))
print(N-max(C))
