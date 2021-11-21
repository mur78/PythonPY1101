def output_type_list(fn):
    def wrapper(*args, **kwargs):

        result = fn(*args, **kwargs)
        if not isinstance(result, list):
            raise TypeError(f"Результатом выполнения функции {fn} должен быть список")

    return wrapper


@output_type_list
def return_list() -> list:
    return []


@output_type_list
def return_tuple() -> str:
    return ""


if __name__ == "__main__":
    return_list("1", "3")
    return_tuple("1", "7")
