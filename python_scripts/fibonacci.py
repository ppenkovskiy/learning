print('Please enter n: ')
num = int(input())


def fibonacci(n):
    if n == 1:
        res = [0, ]
    elif n == 2:
        res = [0, 1]
    else:
        res = [0, 1]
        for i in range(3, n + 1):
            res.append(res[-1] + res[-2])
    print(*res, sep='\n')


fibonacci(num)