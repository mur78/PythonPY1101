def print_args(*args):
    print(type(args), args)


def print_kwargs(**kwargs):
    print(type(kwargs), kwargs)


def print_args_kwargs(*args, **kwargs):
    for index, arg in enumerate(args):
        print(f"Позиционный аргумент {index}: {arg}")

    for key, kwarg in kwargs.items():
        print(f"Именованный аргумент {key}: {kwarg}")


if __name__ == "__main__":
    print_args('j', 'v', 'p')
    print_kwargs(t1 = 5, t2 = "l")

    print_args_kwargs(y = 3, z = 5)

