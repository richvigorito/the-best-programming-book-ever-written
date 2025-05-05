def power_of_two_negative(n=10):
    digits = [1] + [0] * (n - 1)

    for _ in range(n):
        print('\n.', end='')  
        r = 0
        for i in range(n):
            r = 10 * r + digits[i]
            digits[i] = r // 2
            r = r % 2
            print(digits[i], end='')
    print()

power_of_two_negative(100)
