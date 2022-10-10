# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

 

new_list2 = [2, 3, 4, 5, 6]
new_list = [2, 3, 5, 6]
product_of_list = []
lengh_of_list = len(new_list)
if lengh_of_list % 2 == 0:
    j = int(lengh_of_list / 2)
    for i in range(0,j):
        product_of_list.append(new_list[i]*new_list[-i-1])
else:
    k = int(lengh_of_list / 2 + 1)
    for some_of in range(0,k):
        product_of_list.append(new_list[some_of]*new_list[-some_of-1])
for y in product_of_list:
    print(y)