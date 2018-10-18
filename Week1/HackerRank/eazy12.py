def count_substring(string, sub_string):
    cnt = 0
    cnt1 = 0
    for i in range(len(sub_string)):
        for j in range(len(string)):
            if sub_string[i] == string[j]:
                cnt += 1
                break
        if cnt == 3:
            cnt1 += 1
    return cnt1
s = input()
ss = input()
count_substring(s, ss)