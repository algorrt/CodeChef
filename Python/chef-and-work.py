total = int(input())

for i in range(total):
    f = (input().split(' '))
    n = int(f[0])
    k = int(f[1])
    arr = list(map(int, input().split(' ')))
    #print(n, k, list(arr))

    trips = 0
    weight = 0
    counter = 0
    if max(arr) > k:
        print(-1)

    else:
        for l in range(n-1):
            new = arr[l+1] + arr[l]
            if new <= k:
                arr[l+1] = new
            else:
                trips += 1

        print(trips+1)
