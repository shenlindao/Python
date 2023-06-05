# Напишите программу, которая принимает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.

text = 'a a a b c a a d c d d'
my_list = text.split()
dictionary = {}
count = str()

for letter in my_list:
    if letter in dictionary.keys() :
        dictionary[letter] += 1
        count += f'{letter}_{dictionary[letter]} '
    else :
        dictionary[letter] = 0
        count += f'{letter} '
print(text)
print(count)
