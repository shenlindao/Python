n = int(input("Введите число n: "))

if n == 0 or n == 1 :
    print(f'{n}! = 1')
else:
    res = 1
    i = 2
    while i <=n:
        res *= i
        i += 1

print(f'{n}! = {res}')