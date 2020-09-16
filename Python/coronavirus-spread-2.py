def input_array(arr, struc):
    return (list(map(struc, arr.split())))


def dictsort(counter, i):
    return sorted(counter.items(), key=lambda item: item[i])


n = int(input())

for i in range(n):
    lena = int(input())
    arr = input_array(input(), int)
    lcount = lena
    mcount = 1

    for j in range(lena):
        mx = max(arr[:j+1])
        mn = min(arr[j:])

        mk = len([i for i in arr[:j] if i > mn])
        lk = len([i for i in arr[j+1:] if i < mx])

        lcount = min(lcount, mk+lk+1)
        mcount = max(mcount, mk+lk+1)
        #print(mk, lk)

    f = [lcount, mcount]
    print(*f)
