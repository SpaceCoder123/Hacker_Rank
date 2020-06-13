actual_return=list(map(int,input().split()))
expected_return=list(map(int,input().split()))
yeardiff= (-expected_return[2]+actual_return[2])
monthdiff=(-expected_return[1]+actual_return[1])
daydiff=(-expected_return[0]+actual_return[0])

if yeardiff!=0 and yeardiff>=0:
    print(10000)
elif yeardiff==0 and monthdiff!=0 and monthdiff>=0:
    print(monthdiff*500)
elif yeardiff==0 and monthdiff==0 and daydiff!=0 and daydiff>=0:
    print(daydiff*15)
else:
    print(0)
