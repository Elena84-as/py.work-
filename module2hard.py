from random import randint


def trap(n):
    unique = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                unique += str(i) + str(j)
    return f'{n} - {unique}\nПоздравляю вас'


n = randint(3, 20)
print('Рандом решит твою судьбу')

indiana_jons = trap(n)
print(indiana_jons)


















