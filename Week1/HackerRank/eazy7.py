if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(0, n):
        arr.append(int(input()))
    maxi = 0
    cnt = 0
    for i in range (0, n):
        if arr[i] > maxi:
            maxi = arr[i]
            cnt += 1
        if cnt == n-1:
            print(arr[i])