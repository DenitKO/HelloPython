list1 = [1,2,3,4,5]
list2 = list1

list2[0] = 123 # меняется переменная в обоих списках
list1.pop() # удаляет последний эллемент в списке

for e in list1:
    print(e) # [123,2,3,4]

print()

for e in list2:
    print(e) # [123,2,3,4]

print(list1.insert(2, 11))
print(list1) # [123, 2, 11, 3, 4]