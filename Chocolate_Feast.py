def chocolateFeast(cash, cost, wrapper_cost):    

    chocolate = cash//cost
    wrappers = chocolate

    while wrappers // wrapper_cost > 0:
        new_chocolate = wrappers // wrapper_cost
        wrappers -= new_chocolate * wrapper_cost
        wrappers += new_chocolate
        chocolate += new_chocolate
        
    return chocolate

x=int(input())
for i in range(x):
    a,b,c=map(int,input().split())
    print(chocolateFeast(a,b,c))
