import json

def task() -> str:
    dict_numbers = {n: n ** 2 for n in range(1,11)}  # TODO c помощью dict comprehension сформировать словарь
       # TODO сеализовать словарь в JSON строку
    return json.dumps(dict_numbers, indent=4)

if __name__ == "__main__":
    print(task())
