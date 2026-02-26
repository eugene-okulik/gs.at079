def finish_decor(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print()
        print('finished')
        return result
    return wrapper


@finish_decor
def example(*args, **kwargs):
    print(args, kwargs)


example(1, 2, aaa=3)
