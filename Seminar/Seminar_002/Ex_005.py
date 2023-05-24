#Задача №11. Решение в группах
#Дано натуральное число A > 1. Определите, каким по
#счету числом Фибоначчи оно является, то есть
#выведите такое число n, что φ(n)=A. Если А не
#является числом Фибоначчи, выведите число -1.

number = int(input(" Введите число: "))
count = 2
f1 = 0
f2 = 1
for i in range(int(number)+1):
    f = f1 + f2
    f1 = f2
    f2 = f
    count = count + 1
    if f == number:
        print(count)
        break
    elif f > number:
        print(-1)
        break