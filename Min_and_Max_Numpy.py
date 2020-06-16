import numpy as np 
x,y=map(int,input().split())
my_arr=[]
for i in range(x):
    my_arr.append(list(map(int,input().split())))
z=np.array(my_arr)
print(max(np.min(z,axis=1)))
