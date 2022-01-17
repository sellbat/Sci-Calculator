import itertools

n1 = input(": ")
n = int(n1)
array = [0] * n
for x in range(1, n + 1):
    u = x - 1
    array[u] = x
all_combination = []
for r in range(n + 1):
    combinations_object = itertools.combinations(array, r)
    combination_list = list(combinations_object)
    all_combination += combination_list
for i in range(0, n + 1):
    all_combination.pop(0)
print(all_combination)
m1 = input("number of attributes: ")
m = int(m1)
z = []
a = [z] * m
p = [0] * m
for i in range(m):
    a[i] = input("input: ")
for h in range(m):
    g = input("Attributes for the scales: ")
    p[i] = float(g)
sum1 = []
print(a)
for i in range(m):
    for j in range(len(all_combination)):
        count = 0
        tries = 0
        for h in range(len(all_combination[j])):
            y = str(all_combination[j][h])
            if y in a[i]:
                count = count + 1
            tries = tries + 1
            if tries == len(all_combination[j])&count!=0:
                sum1.append((1 / count) * p[i])
print(sum1)