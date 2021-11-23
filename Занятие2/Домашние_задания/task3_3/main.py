def output_type_int(fn):
    def wrapper(*args, **kwargs):

        # через try exept (итератор проверяем next) - проверяем до результата - используем кортеж и enumerate

        result = fn(*args, **kwargs)
        if not isinstance(result, int):
            raise TypeError("Объект <название или номер позиционного аргумента> <значение аргумента> не является итерируемым")


    return wrapper


@output_type_int
def return_int() -> int:
    pass




if __name__ == "__main__":
    return_int(1, 3)
    return_int("1", "7")
