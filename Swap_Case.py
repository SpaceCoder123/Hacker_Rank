def swap_case(s):
    X=[]
    for i in s:
        if i.islower():
            X.append(i.upper())
        elif i.isupper():
            X.append(i.lower())
        else:
            X.append(i)
    return ''.join(X)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
