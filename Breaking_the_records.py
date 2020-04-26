
x=int(input())
Score=list(map(int,input().split()))

Highest_Scores={}
Lowest_Scores={}
Lowest=0
Highest=0
for i in range(x):
    if i==0:
        Highest_Scores[i]=Score[i]
        Lowest_Scores[i]=Score[i]
        Highest=Score[i]
        Lowest=Score[i]
    elif i>0:
        if Score[i]>Highest :           
            Highest=Score[i]
            Highest_Scores[i]=Score[i]
        elif Score[i]<Lowest:
            Lowest_Scores[i]=Score[i]
            Lowest=Score[i]
print(len(Highest_Scores)-1,len((Lowest_Scores))-1)
