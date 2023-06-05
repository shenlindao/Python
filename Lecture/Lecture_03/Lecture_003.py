def sum_numbers(n, y = 'Hello'):
    print(y)
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

a = sum_numbers(5, 'qwert')
print(a)