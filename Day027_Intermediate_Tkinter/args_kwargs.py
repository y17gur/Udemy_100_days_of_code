def add(*args):
    args_list = []
    for i in args:
        args_list.append(i)
    return sum(args_list)


print(add(1, 2, 3, 4, 5))


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["mult"]
    print(n)


calculate(2, add=3, mult=5)

