
total = int(input())
for j in range(total):
    current_length = int(input())
    counter = 0
    current_word = input()
    all_alphabets = [0] * 26
    for i in range(current_length):
        all_alphabets[ord(current_word[i])-97] += 1
    for i in range(26):
        if all_alphabets[i] % 2 == 1:
            counter = 1
            break
    if counter == 0:
        print('YES')
    else:
        print('NO')
