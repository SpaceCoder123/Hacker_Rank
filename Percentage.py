
n=int(input())
m={}
for i in range(n):
    x=list(input().split())
    x1=x[0]
    x2=x[1::]
    y1=0
    for j in range(len(x2)):      
        y1=y1+float(x2[j])
    average=(y1/len(x2))
    m[x1]=average

name=input()
for k in m:
    if name == k:
        print("{0:.2f}".format(m[k]))
