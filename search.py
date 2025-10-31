import random 
list = random.sample(range(1, 1000000), 100) # Список с рандомными числам
for i in range(99): # выполняем сортировку пузырьком
    for j in range(99-i):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]  # меняем местами
            print(list)  # сортированный список
a = int(input('Введите искомый элемент:'))
d = 0 # счетчик сравнений

for i in range(len(list)): # Линейный поиск
    d += 1 
    if list[i] == a: # если найден нужный элемент, то прекращаем поиск
        break 

d1 = 0 # счетчик сравнений
n = 0
w = len(list) - 1
index = -1
while (n  <= w) and (index == -1): # бинарный поиск
    mid = (n + w) // 2 
    d1 += 1 
    if list[mid] == a: 
        index = mid # Приравние индекса к середине списка 
    else: 
         if a < list[mid]:
            w = mid - 1 
         else:
            n = mid + 1
if index == - 1:   # то есть элемента не нашлось
    print('Элемента нет в списке. ')
else:
    print('Индекс элемента по линейному поиску: ', i)
    print('Количество сравнений при линейном: ', d)
    print('Индекс элемента по бинарному поиску: ', index)
    print('Количество сравнений при бинарном поиске: ', d1)
    
