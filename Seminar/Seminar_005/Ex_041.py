# Задача №41.

# Дан массив, состоящий из целых чисел. 
# Напишите программу, которая в данном массиве определит количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. 
# Массив состоит из целых чисел.


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
for i in range(1, N-1):
    if (array_1[i] > array_1[i-1]) & (array_1[i] > array_1[i+1]):
        count+=1
print(count)