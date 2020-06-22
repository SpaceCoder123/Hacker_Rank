import numpy

def arrays(arr):
    # x=numpy.array(arr)
    # y=[]
    # for i in range(len(x)):
    #     y.append(float(x[len(x)-i-1]))
    # return y 
    (Alternate method)
    return(numpy.array(arr[::-1], float))


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
