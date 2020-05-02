import math
S=list(input())
S1=math.ceil(math.sqrt(len(S)))
for i in range(0,S1):
    print(''.join(S[i::S1]),end=' ') 
