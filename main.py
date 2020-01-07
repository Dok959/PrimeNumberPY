n = 2


def search(n):
    while True:
        k = 2
        f = True
        while k*2 <= n:
            if n % k != 0:
                k += 1
            else:
                f = False
                break
        if f == True:
            return n
        n += 1


while True:
    x = input("Желаете продолжить поиск простого числа? y/n ")
    if x.lower().startswith('y'):
        n = search(n)
        print("Следующее простое число: ", n)
        n += 1
    else:
        break
