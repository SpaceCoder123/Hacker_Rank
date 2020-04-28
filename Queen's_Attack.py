import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    L=c_q-1
    R=n-c_q
    U=n-r_q
    D=r_q-1
    UL=L if U>=L else U
    UR=R if U>=R else U
    DL=L if D>=L else D
    DR=R if D>=R else D
    for x in obstacles:
        ROW=x[0]
        COL=x[1]

        if ROW==r_q and COL<c_q:
            if c_q-COL-1<L:
                L=c_q-COL-1
        elif ROW==r_q and COL>c_q:
            if COL-c_q-COL-1<R:
                R=COL-c_q-1
        elif ROW>r_q and COL==c_q:
            if ROW-r_q-1 < U:
                U=ROW-r_q-1
        elif ROW<r_q and COL==c_q:
            if r_q-ROW-1 < D:
                D=r_q-ROW-1
        elif ROW>r_q and COL<c_q:
            if ROW-r_q ==c_q-COL:
                if ROW-r_q-1<UL:
                    UL=ROW-r_q-1
        elif ROW>r_q and COL>c_q:
            if ROW-r_q==COL-c_q:
                if ROW-r_q-1<UR:
                    UR=ROW-r_q-1
        elif ROW<r_q and COL<c_q:
            if r_q-ROW==c_q-COL:
                if r_q-ROW-1<DL:
                    DL=r_q-ROW-1
        elif ROW<r_q and COL>c_q:
            if r_q-ROW==COL-c_q:
                if r_q-ROW-1<DR:
                    DR=r_q-ROW-1       
    attack=L+R+U+D+UL+UR+DL+DR
    return attack
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
