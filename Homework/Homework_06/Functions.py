def input_array(size):
    array = []
    for i in range(size):
        input_element = int(input(f'Введите элемент №{i+1} массива: '))
        array.append(input_element)
    return array