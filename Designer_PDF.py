import string
alpha=list(string.ascii_lowercase)
values=list(map(int,input().split()))
h=list(input())
dict={}
for i in range(len(values)):
    dict[alpha[i]]=values[i]
hieght=[]
for i in h:
    if dict.__contains__(i):
        hieght.append(dict[i])
print(max(hieght)*len(hieght))
