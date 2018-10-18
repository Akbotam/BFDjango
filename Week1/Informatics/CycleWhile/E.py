N = int(input())
cnt = 0
cnt1 = 2

if N == 1:
    print(0)
elif N == 2:
    print(1)
else:
    while 2*cnt1 < N:
        cnt1 *= 2
        cnt += 1
    print(cnt)