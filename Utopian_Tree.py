L=0
mydict={}
for i in range(0,60):
    if i<=2 or i==0:
        L=L+1
        mydict[i]=L
    elif i%2==0 and i>2:
        L=L+1
        mydict[i]=L
    elif i%2!=0 and i>2:
        L=L*2
        mydict[i]=L
x=int(input())
for i in range(x):
    y=int(input())
    if mydict.__contains__(y):
        print(mydict[y])
