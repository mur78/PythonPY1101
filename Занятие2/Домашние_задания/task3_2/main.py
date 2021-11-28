
def positive_check_int(fn):
    def wrapper(*args):
        # TODO написать проверку положительности аргумента arg
        #map
        # z = map(positive_check_int, *args)

        for args in *args:
            if isinstance(args, int):
                result = fn(*args)
            elif not isinstance(args, int):
                raise TypeError(f"Результатом выполнения функции {fn} должен быть числом")

        return result

    return wrapper


# TODO задекорировать функцию
@positive_check_int
def some_func():
    pass


if __name__ == "__main__":

    some_func(5, 7, "8")

    #some_func("7", "tn")
