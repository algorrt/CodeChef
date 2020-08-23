def subarrayBitwiseOR(A):
    res = set()
    pre = {0}

    for x in A:
        pre = {x | y for y in pre} | {x}
        res |= pre

    print(res, len(res))
    return len(res)


total = int(input())
for i in range(total):
    count_elements = int(input())
    cur_array = map(int, input().split())
    if subarrayBitwiseOR(cur_array) == pow(2, count_elements) - 1:
        print('YES')
    else:
        print('NO')
