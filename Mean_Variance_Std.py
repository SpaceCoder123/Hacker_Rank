import numpy as np
x=[]
m,n=map(int,input().split())
for i in range(m):
    x.append(list(map(int,input().split())))
x1=np.array(x)
print(np.mean(x1,axis=1))
print(np.var(x1,axis=0))
print(np.std(x1))
