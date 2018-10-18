x = int(input())
cnt = 1
for a in range(2, x+1):
    if x % a == 0:
        cnt += 1
print(cnt)

