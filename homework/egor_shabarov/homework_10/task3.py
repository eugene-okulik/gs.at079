def decorator(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            result = func(first, second, '*')
        elif first == second:
            result = func(first, second, '+')
        elif first > second:
            result = func(first, second, '-')
        elif second > first:
            result = func(first, second, '/')
        return result
    return wrapper


@decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

print(calc(a, b))
