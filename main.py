n = 1


def search(n):
    while True:
        k = 2
        f = True
        n += 1
        while k*2 <= n:
            if n % k != 0:
                k += 1
            else:
                f = False
                break
        if f == True:
            return n


while True:
    x = input("Желаете продолжить поиск простого числа? y/n ")
    if x.lower().startswith('y'):
        n = search(n)
        print("Следующее простое число: ", n)
    else:
        break
