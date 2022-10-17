# Фунция map

li = [x for x in range(1,20)]

li2 = list(map(lambda x:x+10, li))

print(li2)

# # 1 ввод
# data = list(map(int, input().split()))

# print(data)

# # 2 ввод
# data2 = map(int,input().split())

# for e in date:
#     print(e)

# # 3 ввод
# data3 = list(map(int, '1 2 3 4 55 6'.split()))

# for e in data3:
#     print(e*10)

# print(data3)

# 4 ввод
data4 = [x for x in range(10)]

res = list(filter(lambda x: x%2==0, data4))
# print(res)