n = int(input('Введите число n:'))
min = 100
max = 0

for i in range(n) :
    x = int(input('Введите массу арбуза:'))
    if x > max :
        max = x
    if x < min :
        min = x
        
print('min', min, 'max', max)