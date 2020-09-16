from math import ceil


def input_array(arr, struc):
    return (list(map(struc, arr.split())))


def dictsort(counter, i):
    return sorted(counter.items(), key=lambda item: item[i])


def arrsum(t):
    return(t*(t+1)//2)


n = int(input())

for i in range(n):
    cur = int(input())
    count = 0
    if (cur+3) % 4 == 0 or (cur+2) % 4 == 0:
        print(0)
    else:
        asum = arrsum(cur)
        f1 = ceil(asum ** 0.5) + 1
        mx = cur - 1
        sf1 = arrsum(f1)
        sf2 = asum - sf1
        diff = sf2 - sf1
        while diff//2 <= mx:
            if diff == 0:
                count += arrsum(f1-1)
                count += arrsum(cur-f1-1)
            if diff > 0 and diff % 2 == 0:
                count += min(cur-f1, cur-diff//2, diff//2)
                #print(cur-f1, diff//2, cur-diff//2)

            sf1 -= f1
            sf2 += f1
            f1 -= 1
            diff = sf2 - sf1

            #print(f1, count, diff, mx, sf1, sf2)

        print(count)
