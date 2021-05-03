# import random
# for i in range(10):
#     a = random.randint(0, 10)
#

# print([i for i in range(3)])

a = [5, [1, 2], 2, 'r', 4, 'ee']
b = [4, 'we', 'ee', 3, [1, 2]]
x = []

def spisok(a, b, x):
    for g in a:
        for q in b:
            if g == q:
                x.append(g)
                break
    print(x)

spisok(a, b, x)