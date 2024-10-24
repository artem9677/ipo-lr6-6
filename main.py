import random
arr = [[random.randint(-10,10) for i in range(4)]for j in range(20)]

arr_2 = list()

for i in arr:
    i.sort()

for el in arr:
    if arr.count(el) == 1:
        x = tuple(el)
        arr_2.append(x)


print("Уникальные комбинации:")
print(arr_2)




