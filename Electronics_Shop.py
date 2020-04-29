b,n,m=map(int,input().split())
k=list(map(int,input().split()))
u=list(map(int,input().split()))
MONEY=[]
for i in range(len(k)):
    for j in range(len(u)):
        if k[i]+u[j] <=b:
            MONEY.append(k[i]+u[j])
if len(MONEY)>0:
    print(max(MONEY))
else:
    print('-1')
