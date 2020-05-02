L,T=map(int,input().split())
Arr=list(map(int,input().split()))
for i in range(T):
    x,y=map(int,input().split())
    print(min(Arr[x:y+1]))
