with open("test.txt", "r") as f:
    data = f.read().splitlines()

answer = []

for number in data:
    print(number)
    double_x = None
    check_sum = 0

    for character in number[-2::-2]:
        if character == 'X':
            double_x = True
            continue
        if int(character) * 2 < 10:
            check_sum += int(character) * 2
        else:
            check_sum += (int(character) * 2) - 9

    for character in number[-3::-2]:
        if character == 'X':
            double_x = False
            continue
        check_sum += int(character)

    if double_x is None:  # X is the check digit at the end
        for i in range(10):
            if (check_sum + i) % 10 == 0:
                print(i)
                answer.append(str(i))
                break
        continue

    check_digit = int(number[len(number) - 1])

    for i in range(10):
        j = i
        if double_x:
            j = i * 2
            if j >= 10:
                j = j - 9
        if (check_sum + j + check_digit) % 10 == 0:
            print(i)
            answer.append(str(i))
            break
        elif i == 9:
            print("Digit not found, calculated sum:", check_sum)

print(''.join(answer))
print(len(answer))
