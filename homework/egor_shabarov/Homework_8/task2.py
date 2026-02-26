def fib_gen():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


gen = fib_gen()
count = 1

for item in gen:
    if count in [5, 200, 1000]:
        print(item)
    elif count == 100000:
        print(item)
        break
    count += 1
