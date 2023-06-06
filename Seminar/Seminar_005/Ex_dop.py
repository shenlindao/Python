# Рекурсия палиндром
# 'шалаш'
# 'asdffdsa'
# '' 'a'

def palindrom(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrom(s[1:-1])

N = input('Введите любую строку для проверки на палиндром: ')
print(palindrom(N))
