def repeat_me(func):
    def wrapper(*args, count=1):
        for i in range(count):
            result = func(*args)
        return result
    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=3)
