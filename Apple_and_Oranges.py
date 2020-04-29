s,t=map(int,input().split())
a,b=map(int,input().split())
m,n=map(int,input().split())
d1=list(map(int,input().split()))
d2=list(map(int,input().split()))
K=0
for i in d1:
    D1=a+i
    if D1>=s and D1<=t:
        K=K+1
L=0
for j in d2:
    D2=b+j
    if D2>=s and D2<=t:
        L=L+1
print(K)
print(L)
