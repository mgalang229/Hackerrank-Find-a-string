def count_substring(string, sub_string):
    cnt = 0
    for i in range(len(string)):
        ok = True
        if i+len(sub_string) <= len(string):
            for j in range(len(sub_string)):
                ok &= string[i+j] == sub_string[j]
            cnt += ok
    return cnt

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
