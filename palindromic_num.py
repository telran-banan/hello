def palindrom_check(num):
    list = str(num % 10)
    num = num // 10
    while num != 0:
        list = list + str(num % 10)
        num = num // 10
    return list

def show_palindromic_list(start, stop):
    list = []
    step = 1
    if start > stop:
        step = -1
    for num in range(start, stop + step, step):
        if palindrom_check(num) == str(num):
            list.append(num)
    return list

print(show_palindromic_list(10,100))

print(show_palindromic_list(10, 100))