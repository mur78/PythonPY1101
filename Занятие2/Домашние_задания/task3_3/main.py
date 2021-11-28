def output_type_l(fn):
    def wrapper(*args, **kwargs):
        try:
        next(*args)
        next(**kwargs)
        # через try exept (итератор проверяем next) - проверяем до результата - используем кортеж и enumerate
            for index, arg in enumerate(args):
                print(f"Позиционный аргумент {index}: {arg}")

            for key, kwarg in kwargs.items():
                print(f"Именованный аргумент {key}: {kwarg}")

                result = fn(*args, **kwargs)

            except StopIteration:
            print("Итератор закончился")
            print_exc()

# if not isinstance(result, int):
            #     raise TypeError("Объект <название или номер позиционного аргумента> <значение аргумента> не является итерируемым")


    return wrapper


@output_type_l
def return_list() -> list:
    pass

@output_type_l
def return_dict() -> dict:
    pass





if __name__ == "__main__":
    return_list(1, 3)
    return_dict(t1=5, z1=7)

