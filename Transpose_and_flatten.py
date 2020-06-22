import numpy as np
n,m=map(int,input().split())
input_numbers=[]
for i in range(0,n):
    input_numbers.append(list(map(int,input().split())))

Input=np.array(input_numbers)
print(np.transpose(Input))
print(Input.flatten())
