x1=list(map(int,input().split()))
given=list(map(str,input().split(' ')))
A=set(map(str,input().split(' ')))
B=set(map(str,input().split(' ')))

Happy=0
for i in given:
    if i in A:
        Happy=Happy+1
    elif i in B:
        Happy=Happy-1
    else:
        Happy=Happy+0
print(Happy)
