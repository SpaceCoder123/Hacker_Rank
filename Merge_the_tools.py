def merge_the_tools(string, k):
    string_1=list(string)
    for i in range(0,k):
        dict_1={}
        curr_list=string[i*k:k*(i+1)]
        s=''
        for j in curr_list:
            if dict_1.__contains__(j):
                continue
            else:
                dict_1[j]=curr_list.count(j)
                s=s+j
        print(s)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
