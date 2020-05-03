Given_date=list(map(int,input().split()))
Expected_Date=list(map(int,input().split()))

Year_Diff=(Given_date[2]-Expected_Date[2])
Month_Diff=(Given_date[1]-Expected_Date[1])
Day_Diff=(Given_date[0]-Expected_Date[0])

if Year_Diff==0:
    if Month_Diff==0:
        if Day_Diff>0:
            print(15*Day_Diff)
        elif Day_Diff<=0:
            print(0)
    elif Month_Diff>0:
        print(500*(Month_Diff))
    elif Month_Diff<0:
        print(0)
elif Year_Diff>0:
    print(10000)
elif Year_Diff<0:
    print(0)
