import random
list = [] # список 
q = 0 # счетчик сравнений 
for i in range(100):
    list.append(random.randint(1, 1000000))  # в список добавляется случайное число от 1 до 1000000
print(list)  # вывод неотсортированного списка
for i in range(99): # выполняем сортировку пузырьком
    for j in range(99-i):
        q += 1
        if list[j] < list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]  # меняем местами
            print(list)


list1 = [] # список
d = 0 # счетчик сравнений 
for i in range(100):
    list1.append(random.randint(1, 1000000))  
print(list1) 
a = 0 # выполняем сортировку выбором
while a < 99:
    m = a 
    w = a + 1
    while w < 100:
        if list1[w] < list1[m]:
            m = w
        w += 1
        d += 1
    list1[a], list1[m] = list1[m], list1[i] # меняем местами
    a += 1
    print(list1)
print ('Количество сравнений, сделанных в сортировке пузырьком:', q)
print('Количество сравнений, сделанных в сортировке выбором', d)
    


