# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так:
#  [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
f = int(input('Введите целое положительное число '))
new_list = []
new_list2 = []
new_list3 = []

for i in range(0,f+1):
    if i == 0:
        new_list.append(0)
    elif i == 1:
        new_list.append(1)
    else:
        new_list.append(new_list[i-2]+new_list[i-1])

for k in range(0,f+1):
    if k == 0:
        new_list2.append(0)
    elif k == 1:
        new_list2.append(1)
    else:
        new_list2.append(new_list2[k-2]-new_list2[k-1])
    
for rev1 in range(1,f+1):
    new_list3.append(new_list2[-rev1])
for rev2 in range(0,f+1):
    new_list3.append(new_list[rev2])

for v in new_list3:
    print(v, end=' ')