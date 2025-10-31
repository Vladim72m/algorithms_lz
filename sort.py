import random
list = []
for i in range(0, 9):
    list.append(random.randint(1, 1000000))
print(list) 
for i in range(9-1):
    for j in range(9-1-i):
        if list[j] < list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
            print(list)
print ('////////////////////////')


list1 = []
for i in range(0, 9):
    list1.append(random.randint(1, 1000000))
print(list1) 
a = 0 
while a < 9 - 1:
    m = a 
    w = a + 1
    while w < 9:
        if list1[w] < list1[m]:
            m = w
        w += 1
    list1[a], list1[m] = list1[m], list1[i]
    a += 1
    print(list1)