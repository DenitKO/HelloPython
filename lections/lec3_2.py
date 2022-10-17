# List Comprehension

# 1. [exp for item in iterible]
# 2. [exp for item in iterible (if conditional)]
# 3. [exp <if conditional> for item in iterible (if conditional)] 

list = []

for i in range(1, 21):
    if(i%2 == 0):
        list.append(i)

print(list)

list2 = [(i, i+1) for i in range(1,21) if i%2 == 0]

print(list2)

def f(x):
    return x**3

list3 = [(i, f(i)) for i in range(1,21) if i%2 == 0]

print(list3)