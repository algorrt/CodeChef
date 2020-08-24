total = int(input())

for i in range(total):
    sides = int(input())
    for j in range(sides):
        temp = input()

    final = sides
    while sides > 5:
        final += sides // 2
        sides = sides // 2

    print(final)
