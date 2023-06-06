# Задача №43. Решение в группах

# Дан список чисел. 
# Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список чисел. 
# Все числа списка находятся на разных строках.


def input_array(size):
    array = []
    for i in range(size):
        input_element = int(input(f'Введите элемент №{i+1} массива: '))
        array.append(input_element)
    return array

N = int(input('Введите количество элементов массива: '))    
array_1 = input_array(N)
print(array_1)

count=0
for i in range(N):
    for j in range(i + 1, N):
        if array_1[i] == array_1[j]:
            count += 1
print(count)