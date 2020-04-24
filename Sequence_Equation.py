x=int(input())
Given=list(map(int,input().split()))
m={}
for i in range(1,x+1):
    m[i-1]=Given[i-1]+1

print(m)



    