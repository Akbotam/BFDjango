N = int(input())
cnt = 0

for x in range(1, N+1):
    x = int(input())
    if x * 5 == 0:
        cnt += 1

print(cnt)