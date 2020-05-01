n=int(input())
dic={}
for i in range(n):
    k,v=map(str,input().split())
    dic[k]=v
for i in range(n):
    k1=input()
    if dic.__contains__(k1):
        print("{}={}".format(k1,dic[k1]))
    else:
        print('Not found')
