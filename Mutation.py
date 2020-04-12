def mutate_string(string, n, char1):
    string1=list(string)
    for i in range(len(string1)):
        if i==n:
            string1[i]=char1
    x="".join(string1)
    return x

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
