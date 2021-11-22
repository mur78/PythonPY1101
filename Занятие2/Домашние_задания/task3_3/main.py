def output_type_int(fn):
    def wrapper(*args, **kwargs):

        result = fn(*args, **kwargs)
        if not isinstance(result, int):
            raise TypeError("Объект <название или номер позиционного аргумента> <значение аргумента> не является итерируемым")


    return wrapper


@output_type_int
def return_int() -> int:
    return




if __name__ == "__main__":
    return_list("1", "3")
    return_tuple("1", "7")
