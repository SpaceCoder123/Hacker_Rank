x=int(input())

for i in range(x):
    L=0
    y1=input()
    y=list(y1)
    for i in y:
        if int(i)==0:
            L=L+0
        elif int(y1)%int(i)==0:
            L=L+1
        else:
            L=L+0
    print(L)


    
    

