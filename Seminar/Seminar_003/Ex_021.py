# Напишите программу для печати всех уникальных
# значений в словаре.

myList = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
result = []
for item in myList:
    result.append(list(item.values())[0])
print(set(result))