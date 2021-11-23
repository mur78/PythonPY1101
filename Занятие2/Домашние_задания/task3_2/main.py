
def positive_check_int(fn):
    def wrapper(*args):
        # TODO написать проверку положительности аргумента arg
        #map
        z = map(int, *args)

        result = fn(*args)

        if not isinstance(result, int):
            raise TypeError(f"Результатом выполнения функции {fn} должен быть числом")

        return result

    return wrapper


# TODO задекорировать функцию
@positive_check_int
def some_func(num: int):
    pass


if __name__ == "__main__":

    some_func(5, 7)

    #some_func("7", "tn")
