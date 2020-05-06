n,s=map(int,input().split())
Clouds=list(map(int,input().split()))
k=100
Jump=Clouds[::s]
for i in Jump:
    if i==0:
        k=k-1
    elif i==1:
        k=k-2-1
print(k)
