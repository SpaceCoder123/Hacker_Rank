S=input()
#S1=S.split()
# final=[]
# for i in range(len(S)):
#     if(i==0):
#         print(S[i].upper())
#     elif S[i] == ' ' and i < len(S)-2:
#         # print(S[i+1].upper())
#         i=i+1
#         print(i)
#     else:
#         print(i)
#         print(S[i])
toUpper=True
for x in S:
    if toUpper==True:
        print(x.upper(),end='')
        toUpper=False
    elif x==" ":
        toUpper=True
        print(x,end='')
    else:
        toUpper=False
        print (x,end='')