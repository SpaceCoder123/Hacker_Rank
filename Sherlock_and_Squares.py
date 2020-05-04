import math
T=int(input())
for i in range(T):
    num1,num2=map(int,input().split())
    sqrnum1=math.ceil(math.sqrt(num1))
    sqrnum2=math.floor(math.sqrt(num2))
    x=list(range(sqrnum1,sqrnum2+1))
    print(len(x))
