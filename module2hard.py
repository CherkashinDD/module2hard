import random


def numeric_field_1():
    key_list = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    key = random.choice(key_list)
    return key


n = numeric_field_1()  # Число в первом поле

result = []  # Код для ввода во второе поле

for i in range(1, n):
    for j in range(1, n):
        if i != j and n % (i + j) == 0 and i < j:
            result.append(i)
            result.append(j)
            continue

print("Число в первом поле: ", n)

print("Код для ввода во второе поле: ", *result, sep='')
