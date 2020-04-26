x=list(map(str,input().split(':')))
hour=[]
time=[]
for i in range(len(x[2])):
    if i<2:
        hour.append(x[2][i])
    else:
        time.append(x[2][i])
for j in range(len(hour)):
    x.append((hour[j]))
    x.append((time[j]))
s=''
s=s.join(hour)

if x[4]=='A':
    if int(x[0])<10:
        print('{}'':{}:{}'.format(x[0],x[1],s))
    elif int(x[0])>=10 and int(x[0])<12:
        print('{}:{}:{}'.format(x[0],x[1],s))
    elif int(x[0])==12:
        print('{}:{}:{}'.format('00',x[1],s))
elif x[4]=='P':
    if int(x[0])==12:
        print('{}:{}:{}'.format(x[0],x[1],s))
    else:
        print('{}:{}:{}'.format(str(int(x[0])+12),x[1],s))
