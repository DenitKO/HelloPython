# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

new_list = [10, 2, 100, 5, 1000]
j = 0
sum_of_even = 0
lent_of_list = len(new_list)
while j != lent_of_list-1:
    if j%2:
        sum_of_even = sum_of_even + new_list[j]
    j = j + 1
print(f'сумма = {sum_of_even}')