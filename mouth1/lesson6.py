a = [5, [1, 2], 2, 'r', 4, 'ee']
b = [4, 'we', 'ee', 3, [1, 2]]     `
for i in a:
    for j in b:
        if i == j:
            c.append(i)
            break

print(c)`