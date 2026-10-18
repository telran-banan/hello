import random

def exists(numbers, num):
    for n in numbers:
        if n == num:
            return True
    return False

def get_random_numbers(min, max, size):
    list = []
    if size > max - min + 1:
        return list
    count = 0
    while count < size:
        num = random.randint(min, max)
        if not exists(list, num):
            list.append(num)
            count = count + 1
    return list

print(get_random_numbers(1, 49, 7))