n=int(input())
x=input().split()
runner=int(min(x))
winner=int(max(x))

for i in range(n):
    if int(x[i])>winner:
        runner=winner
        winner=int(x[i])
    elif int(x[i]) > runner and int(x[i])< winner:
        runner=int(x[i])

print(runner)
