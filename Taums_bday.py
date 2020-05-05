T=int(input())
def taumBday(b, w, bc, wc, z):
    return b*min(bc, wc+z) + w*min(wc,bc+z)

for i in range(T):
    b,w=map(int,input().split())
    bc,wc,z=map(int,input().split())
    print(taumBday(b,w,bc,wc,z))
