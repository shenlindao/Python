a = int(input('Введите число a>1: '))
x = 0
y = 1
count = 3

while x + y < a:
    count += 1
    temp = x
    x = y   
    y = temp + y

if x + y == a:
    print(count)
else:
    print(f'F(-1)')