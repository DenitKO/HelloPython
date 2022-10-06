from ast import For
import lec1 as l

print (l.f(1))

def new_string(symbol, count = 3):
    return symbol * count

print(new_string('!',5)) # !!!!!
print(new_string('!'))   # !!!
print(new_string(4))     # 12


# Можно поставить перед аргументом функции звездочку для того,
# чтобы указывать бесконечнечное количество переменных
def concatenatio(*params):
    res: str = "" # Явное указание переменных
    for item in params:
        res += item
    return res

print(concatenatio('a','s','d','w')) # asdw
print(concatenatio('a','1','d','2')) # a1d2
# print(concatenatio('1','2','3','4')) # TypeError: ...

def concatenatio(*params):
    res: int = 0 # Явное указание переменных
    for item in params:
        res += item
    return res

# print(concatenatio('a','s','d','w')) # asdw
# print(concatenatio('a','1','d','2')) # a1d2
print(concatenatio('1','2','3','4')) # TypeError: ...