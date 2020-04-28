L,M=map(int,input().split())
A=list(map(int,input().split()))
X=max(A)
if X<=M:
    print('0')
else:
    print(abs(M-X))
