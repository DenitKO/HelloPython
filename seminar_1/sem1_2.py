# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print('a = ¬(X ⋁ Y ⋁ Z)')
print('b = ¬X ⋀ ¬Y ⋀ ¬Z')
for X in range(0,2):
    for Y in range(0,2):
        for Z in range(0,2):
            a = not(X|Y|Z)
            b = not X and not Y and not Z
            print(f'X = {X} Y = {Y} Z = {Z} вывод a == b {a == b}')