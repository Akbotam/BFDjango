def swap_case(s):
    for i in range(0, len(s)):
        if(s[i] >= 'a' and s[i] <= 'z'):
            s[i].upper()
        else:
            s[i].lower()
    return s
s = input()
swap_case(s)