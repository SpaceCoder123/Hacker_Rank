Q=int(input())
for i in range(Q):
    C1,C2,M1=map(int,input().split())
    D1=abs(C1-M1)
    D2=abs(C2-M1)
    if D1>D2:
        print('Cat B')
    elif D1<D2:
        print('Cat A')
    elif D1==D2:
        print('Mouse C')
